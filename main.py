import offline_functions
import online_functions
from offline_functions import openFile


def testFunc():
    openFile.openFile('"C:\\Riot Games\\Riot Client\\RiotClientServices.exe" --launch-product=league_of_legends '
                      '--launch-patchline=live')


testFunc()
