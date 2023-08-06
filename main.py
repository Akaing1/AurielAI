from offline_functions import openFile
from online_functions import checkWeather
from online_functions import googleSearch


def testOpenFile():
    openFile.openFile('"C:\\Riot Games\\Riot Client\\RiotClientServices.exe" --launch-product=league_of_legends '
                      '--launch-patchline=live')


def testCheckWeather():
    details = checkWeather.getAllDetails('morrisville')
    print(details[0], details[1], details[2])


def testGoogleSearch():
    search = googleSearch.googleSearch('league of legends')
    print(search)


testGoogleSearch()
