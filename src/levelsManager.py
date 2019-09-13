from level import level
from fileObject import *


class levelsManager:
    def __init__(self, PATH):
        self.__pathToFolder = PATH
        for i in range(getCountOfFilesInFolder(self.__pathToFolder)):
            self.levels.append(level(self.__pathToFolder + "\level" + str(i)+ ".txt"))

    def getCountOfLevels(self):
        return getCountOfFilesInFolder(self.__pathToFolder)

    def getPathToFolder(self):
        return self.__pathToFolder

    levels = []
    __pathToFolder = ""
