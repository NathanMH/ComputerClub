
##################
# Imports
##################

from bs4 import BeautifulSoup
import urllib.request
import pickle
import os

##################
# Functions
##################

# SITE_URL = "https://en.wikipedia.org/wiki/List_of_national_capitals_in_alphabetical_order"
SITE_URL = "http://www.manythings.org/vocabulary/lists/2/words.php?f=countries_and_capitals"

def make_html(site):
    html = urllib.request.Request(site)
    response = urllib.request.urlopen(html)
    return response.read().decode('utf-8')


def make_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def make_and_save_list(soup):
    countries = soup.find_all("b")
    capitals = soup.find_all("i")

    combined_dictionary = {}
    # Make dictionary here to return both simultaneously
    for i in range(0, 193):
        country = countries[i].contents[0].rstrip()
        capital = capitals[i].contents[0].rstrip()
        combined_dictionary[country] = capital

    with open("ccPickle", "wb") as handle:
        pickle.dump(combined_dictionary, handle)

    return combined_dictionary


##################
# Main
##################

def main():
    if os.path.exists("ccPickle") and os.path.getsize("ccPickle") >= 0:
        print("Loading list...")
        with open("ccPickle", "rb") as handle:
            the_list = pickle.load(handle)
        return the_list

    else:
        print("Generating list...")
        soup = make_soup(make_html(SITE_URL))
        the_list = make_and_save_list(soup)
        return the_list

FINAL_LIST = main()

##################
# Testing
##################

# print(FINAL_LIST)

