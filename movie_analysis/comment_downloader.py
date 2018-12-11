#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:16:20 2018

@author: jamie
"""

from __future__ import print_function

import sys
import time
import json
import requests
import lxml.html
import lxml.etree
import pandas as pd
from lxml.cssselect import CSSSelector

YOUTUBE_COMMENTS_URL = 'https://www.youtube.com/all_comments?v={youtube_id}'
YOUTUBE_COMMENTS_AJAX_URL = 'https://www.youtube.com/comment_ajax'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'


def find_value(html, key, num_chars=2):
    pos_begin = html.find(key) + len(key) + num_chars
    pos_end = html.find('"', pos_begin)
    return html[pos_begin: pos_end]


def extract_comments(html):
    tree = lxml.html.fromstring(html)
    item_sel = CSSSelector('.comment-item')
    text_sel = CSSSelector('.comment-text-content')
    time_sel = CSSSelector('.time')
    author_sel = CSSSelector('.user-name')

    for item in item_sel(tree):
        yield {'cid': item.get('data-cid'),
               'text': text_sel(item)[0].text_content(),
               'time': time_sel(item)[0].text_content().strip(),
               'author': author_sel(item)[0].text_content()}

def extract_reply_cids(html):
    tree = lxml.html.fromstring(html)
    sel = CSSSelector('.comment-replies-header > .load-comments')
    return [i.get('data-cid') for i in sel(tree)]


def ajax_request(session, url, params, data, retries=10, sleep=20):
    for _ in range(retries):
        response = session.post(url, params=params, data=data)
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            return response_dict.get('page_token', None), response_dict['html_content']
        else:
            time.sleep(sleep)


def download_comments(youtube_id, sleep=1):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT

    # Get Youtube page with initial comments
    response = session.get(YOUTUBE_COMMENTS_URL.format(youtube_id=youtube_id))
    html = response.text
    reply_cids = extract_reply_cids(html)
    text = []

    ret_cids = []
    for comment in extract_comments(html):
        ret_cids.append(comment['cid'])
        text.append(str(comment['text']))

    page_token = find_value(html, 'data-token')
    session_token = find_value(html, 'XSRF_TOKEN', 4)

    first_iteration = True

    # Get remaining comments (the same as pressing the 'Show more' button)
    while page_token:
        data = {'video_id': youtube_id,
                'session_token': session_token}

        params = {'action_load_comments': 1,
                  'order_by_time': True,
                  'filter': youtube_id}

        if first_iteration:
            params['order_menu'] = True
        else:
            data['page_token'] = page_token

        response = ajax_request(session, YOUTUBE_COMMENTS_AJAX_URL, params, data)
        if not response:
            break

        page_token, html = response

        reply_cids += extract_reply_cids(html)
        for comment in extract_comments(html):
            if comment['cid'] not in ret_cids:
                ret_cids.append(comment['cid'])
                text.append(str(comment['text']))

        first_iteration = False
        time.sleep(sleep)

    # Get replies (the same as pressing the 'View all X replies' link)
    for cid in reply_cids:
        data = {'comment_id': cid,
                'video_id': youtube_id,
                'can_reply': 1,
                'session_token': session_token}

        params = {'action_load_replies': 1,
                  'order_by_time': True,
                  'filter': youtube_id,
                  'tab': 'inbox'}

        response = ajax_request(session, YOUTUBE_COMMENTS_AJAX_URL, params, data)
        if not response:
            break

        _, html = response

        for comment in extract_comments(html):
            if comment['cid'] not in ret_cids:
                ret_cids.append(comment['cid'])
                text.append(str(comment['text']))
        time.sleep(sleep)
    return text

def write_csv(youtube_id, movie_id):
    comments = download_comments(youtube_id)
    df = pd.DataFrame({'comments':comments})
    filename = str(movie_id) + '.csv'
    df.to_csv(filename, encoding='UTF-8', index=False)

def download_from_list(input_file):
    for i in range(len(input_file)):
        youtube_id = input_file['youtube_id'][i]
        movie_id = input_file['movie_id'][i]          
        if not youtube_id or not movie_id:
            raise ValueError('you need to specify a youtube_id and a movie_id')          
        print('Downloading Youtube comments for video:', youtube_id)
        write_csv(youtube_id, movie_id)     
    print('\nDone!')

def main(argv):
    try:
        filename = argv
        input_file = pd.read_csv(filename, sep=',')
        for i in range(len(input_file)):
            youtube_id = input_file['youtube_id'][i]
            movie_id = input_file['movie_id'][i]
            if not youtube_id or not movie_id:
                raise ValueError('you need to specify a youtube_id and a movie_id')
            print('Downloading Youtube comments for video:', youtube_id)
            write_csv(youtube_id, movie_id)
        print('\nDone!')
    except Exception as error_details:
        print('Error:', str(error_details))
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1])
