
##################
# Imports
##################

from bs4 import BeautifulSoup
import urllib.request


##################
# Functions
##################

# url = "https://en.wikipedia.org/wiki/List_of_national_capitals_in_alphabetical_order"
url = "http://www.manythings.org/vocabulary/lists/2/words.php?f=countries_and_capitals"


def make_html(url):
    html = urllib.request.Request(url)
    response = urllib.request.urlopen(html)
    return response.read().decode('utf-8')


def make_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def make_list(soup):
    countries = soup.find_all("b")
    capitals = soup.find_all("i")

    combined_dictionary = {}
    # Make dictionary here to return both simultaneously
    for i in range(0, 193):
        country = countries[i].contents[0].rstrip()
        capital = capitals[i].contents[0]
        combined_dictionary[country] = capital
    return combined_dictionary

##################
# Main
##################

def main():
    soup = make_soup(make_html(url))
    return make_list(soup)

final_list = main()
##################
# Testing
##################

print(final_list)

