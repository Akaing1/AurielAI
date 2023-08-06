from online_functions import checkWeather
from online_functions import googleSearch


def testCheckWeather():
    details = checkWeather.getAllDetails('morrisville')
    print(details[0], details[1], details[2])


def testGoogleSearch():
    search = googleSearch.googleSearch('league of legends')
    print(search)


def runTests():
    testCheckWeather()
    testGoogleSearch()