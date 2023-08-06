import requests
from bs4 import BeautifulSoup


def getTemperature(city):

    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    return temp


def getAllDetails(city):

    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    s = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = s.split('\n')
    time = data[0]
    sky = data[1]

    return [temp, time, sky]





