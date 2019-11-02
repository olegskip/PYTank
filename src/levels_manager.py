from level import Level
from file import *
import config
import random


class LevelsManager:
    def __init__(self, PATH):
        self.__folderPath = PATH
        for i in range(get_folder_files_count(self.__folderPath)):
            self.levels.append(Level(self.__folderPath + "\level" + str(i) + ".txt"))
        print(str("\nLoading " + str(len(self.levels)) + " level(s) in " + self.get_folder_path()))
        for item in self.levels:
            try:
                item.get_file_data()
            except FileNotFoundError:
                print("ERROR 404! " + item.get_path())
            else:
                print("Loading " + item.get_path())

        self.current_level_index = 0
        self.update_index()

    def get_folder_path(self):
        return self.__folderPath

    def update_index(self):
        new_level_index = self.current_level_index
        while new_level_index == self.current_level_index:
            if len(self.levels) == 1:  # if is only one level in folder that the level can't but repeat
                break
            new_level_index = random.randint(0, len(self.levels) - 1)
        self.current_level_index = new_level_index

    levels = []
    __folderPath = ""

    current_level_index = 0

lvlManager = LevelsManager(config.PATH_TO_LEVELS)
