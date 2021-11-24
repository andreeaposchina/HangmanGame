from core.settings import *
from random import choice
from os import path
from core.file_handler_class import FileHandler


class History:
    def __init__(self, filename):
        self.filename = filename
        self.file_handler = FileHandler(self.filename)

    def choose_word(self) -> str:
        """
        This method is used to choose a random word from a given file
        :return: It returns string which represents the word
        """
        lst = self.file_handler.read_lines()
        return choice(lst)

    def build_history(self, data: str):
        """
        This method is used to keep track of the history of players and their progress.
        If the file exists, then this method will overwrite the existing file. If not, then the file will be created,
        and the data will be written.
        :param data: Must be a string
        :return: This method does not return something.
        """
        if path.isfile(BASE_DIR_PATH + "\\" + self.filename):
            existing_data = self.file_handler.read_file()
            data = existing_data + data
            self.file_handler.write_file(data)
        else:
            self.file_handler.write_file(data)

    def build_ranking(self):
        """
        This method is used to sort the data within the file that contains the progress of
        players in order to create a ranking.
        :return: This method does not return something.
        """
        data = self.file_handler.read_lines()
        data_list = [elem.split(',') for elem in data]
        data_list = [[elem.strip() for elem in sublist] for sublist in data_list]

        sorted_list = sorted(data_list, key=lambda x: int(x[1].strip()), reverse=True)

        ranked_list = [', '.join(elem for elem in sublist) for sublist in sorted_list]
        data = ' \n'.join(elem for elem in ranked_list) + '\n'
        self.file_handler.write_file(data)

    def print_ranking(self):
        """
        This method is always returned at the end of a game. It prints the history of plays by making a ranking.
        :return: This method does not return something
        """
        self.build_ranking()

        ranking = self.file_handler.read_lines()
        for line in ranking:
            print(line)
