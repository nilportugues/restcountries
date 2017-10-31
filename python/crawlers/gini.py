from bs4 import BeautifulSoup
import urllib

URL_GINI = 'https://en.wikipedia.org/wiki/List_of_countries_by_income_equality'


def update(countriesJSON):
    html = __getHTML(URL_GINI)
    soup = BeautifulSoup(html, "lxml")
    giniData = __extractGiniData(soup)

    return __updateJSON(countriesJSON, giniData)


def __extractGiniData(html):
    giniData = {}
    for i, row in enumerate(html.table):
        if i > 1:
            for j, column in enumerate(row):
                if j == 1:
                    href = column.find('a')
                    if href is not None:
                        country = href.get_text()
                if j == 7:
                    gini = column.get_text()
                    giniData[country] = gini

    return giniData


def __updateJSON(countriesJSON, giniData):
    for country in giniData:
        for countryJSON in countriesJSON:
            if country == countryJSON['name']:
                if giniData[country]:
                    countryJSON['gini'] = float(giniData[country])

    return countriesJSON


def __getHTML(url):
    usock = urllib.request.urlopen(url)
    data = usock.read()
    usock.close()
    return data
