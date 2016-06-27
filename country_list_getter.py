
##################
# Imports
##################

from bs4 import BeautifulSoup
import urllib.request
import sys


##################
# Functions
##################

#url = "https://en.wikipedia.org/wiki/List_of_national_capitals_in_alphabetical_order"
url = "http://www.manythings.org/vocabulary/lists/2/words.php?f=countries_and_capitals"

def make_da_html(url):
    html = urllib.request.Request(url)
    response = urllib.request.urlopen(html)
    return response.read().decode('utf-8')
   

def make_da_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def make_da_list(soup):
    countries = soup.find_all("b")
    capitals = soup.find_all("i")
    
    # Make dictionary here to return both simultaneously
    for i in range(0, 193):
        combined_dictionary = {countries[i].contents[0]: capitals[i].contents[0]}
    return combined_dictionary

##################
# Main
##################

soup = make_da_soup(make_da_html(url))

make_da_list(soup)

##################
# Testing
##################

