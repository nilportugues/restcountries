# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib

URL_ISO_COUNTRIES = 'https://en.wikipedia.org/wiki/ISO_3166-1'


def update(countriesJSON):
    html = __getHTML(URL_ISO_COUNTRIES)
    soup = BeautifulSoup(html, "html.parser")
    data = __extractData(soup)
    return __updateJSON(countriesJSON, data)


def __getHTML(url):
    usock = urllib.request.urlopen(url)
    data = usock.read()
    usock.close()
    return data

def __extractData(html):
    data = {}
    table = html.findAll('table', class_='wikitable')[1]
    for row in table:
        nameLink = row.find('a')
        if nameLink != -1:
            countryName = nameLink.get_text()
        for idx,element in enumerate(row):
            if idx == 7:
                numericCode = element.text
                data[countryName] = numericCode
        
    return data

def __updateJSON(countriesJSON, data):
    for country in data:
        for countryJSON in countriesJSON:
            if country == countryJSON['name']:
                countryJSON['numericCode'] = data[country]

    return countriesJSON

