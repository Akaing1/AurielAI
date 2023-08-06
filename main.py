import offline_functions
import online_functions
from offline_functions import openFile
from online_functions import checkWeather


def testOpenFile():
    openFile.openFile('"C:\\Riot Games\\Riot Client\\RiotClientServices.exe" --launch-product=league_of_legends '
                      '--launch-patchline=live')


def testCheckWeather():
    temp = checkWeather.getTemperature('morrisville')
    print(temp)
    '''details = checkWeather.getAllDetails('morrisville')
    print(details)'''


testCheckWeather()
