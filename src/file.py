import os


def get_exe_path():
    return os.path.dirname(os.path.abspath(__file__))


def is_file_in_folder(file):
    os.path.exists(file)


def get_folder_files_count(path):
    return len(os.listdir(path))

class File:
    def __init__(self, path):
        self.__path = path

    def get_file_data(self):
        with open(self.__path) as file:
            return [row.strip() for row in file]

    def get_path(self):
        return self.__path

    __path = ""
