from online_functions import checkWeather
from online_functions import googleSearch
from online_functions import checkStocks
from online_functions import watchYoutube


def testCheckWeather():
    details = checkWeather.getAllDetails('morrisville')
    print(details[0], details[1], details[2])


def testGoogleSearch():
    search = googleSearch.googleSearch('league of legends')
    print(search)


def testStockPrice():
    price = checkStocks.getStockPrice('AAPL')
    print(price)


def testStockInfo():
    info = checkStocks.getStockInfo('AAPL')
    print(info)


def testWatchYoutube():
    media = watchYoutube.searchYT('minecraft')
    print(media)


def runTests():
    testCheckWeather()
    testGoogleSearch()
    testStockInfo()
    testStockPrice()
    testWatchYoutube()
