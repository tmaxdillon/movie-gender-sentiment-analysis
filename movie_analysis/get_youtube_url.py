"""This module takes in a  movie title as a string, then appends 'trailer'
and searches for this query on YT. This function returns the URL.
"""

from random import randint
from time import sleep
import requests
from bs4 import BeautifulSoup as bs

def get_first_trailer_url(movie_title):
    """This function takes in a movie title as a string, then appends 'trailer'
    and searches for this query on YT. Returns the URL.
    """
    text_to_search = movie_title + ' trailer'
    text_to_search.replace(" ", "")
    text_to_search.strip()
    query = text_to_search
    url = "https://www.youtube.com/results?search_query=" + query
    try:
        response = requests.get(url)
        html = response.text
        soup = bs(html, 'html.parser')
        list_of_videos = []
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            link = 'https://www.youtube.com' + vid['href']
            list_of_videos.append(link)
        #print(ListOfVideos[1]) #first element is garbage so print second one
        sleep(randint(1, 10))
        return list_of_videos[1]
    except:
        print("There was an error!")
