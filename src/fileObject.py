import os


def getExePath():
    return os.path.dirname(os.path.abspath(__file__))


def getCountOfFilesInFolder(path):
    return len(os.listdir(path))

class fileObject:

    def __init__(self, path):
        self.__path = path

    def getFileData(self):
        return open(self.__path, 'r').read()

    def getPath(self):
        return self.__path

    __path = ""
