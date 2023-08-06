from offline_functions import openFile


def testOpenFile():
    openFile.openFile('"C:\\Riot Games\\Riot Client\\RiotClientServices.exe" --launch-product=league_of_legends '
                      '--launch-patchline=live')


def runTests():
    testOpenFile()

