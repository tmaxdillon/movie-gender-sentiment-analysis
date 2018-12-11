from bs4 import BeautifulSoup as bs
import requests
from random import randint
from time import sleep

#This function takes in a  movie title as a string, then appends 'trailer'
#and searches for this query on YT. This function returns the URL

def get_first_trailerURL(MovieTitle):
    TextToSearch = MovieTitle + ' trailer' #get weird first result if there are spaces
    TextToSearch.replace(" ", "")
    TextToSearch.strip()
    query = TextToSearch
    url = "https://www.youtube.com/results?search_query=" + query
    try:
        response = requests.get(url)
        html = response.text
        soup = bs(html, 'html.parser')
        ListOfVideos = []
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            link = 'https://www.youtube.com' + vid['href']
            ListOfVideos.append(link)
        #print(ListOfVideos[1]) #first element is garbage so print second one
        sleep(randint(1,10))
        return ListOfVideos[1]
    except:
        print("There was an error!")
