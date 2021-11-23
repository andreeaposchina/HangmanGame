from settings import *
from random import choice
from os import path


class Record:
    def __init__(self, filename):
        self.filename = filename

    def read_lines(self) -> list:
        """
        This method is used to read the content of a file by lines.
        :return: A list of lists that contains the lines of the file
        """
        with open(self.filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        return lines

    def read_file(self) -> str:
        """
        This method is used to read the content of a file.
        :return: A string that contains the content of the file
        """
        with open(self.filename, 'r') as file:
            data = file.read()
        return data

    def write_file(self, data: str) -> None:
        """
        This method is used to write data into a file.
        :param data: Must be a string
        :return: This method does not return something.
        """
        with open(self.filename, 'w') as file:
            file.write(data)

    def choose_word(self) -> str:
        """
        This method is used to choose a random word from a given file
        :return: It returns string which represents the word
        """
        lst = self.read_lines()
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
            existing_data = self.read_file()
            data = existing_data + data
            self.write_file(data)
        else:
            self.write_file(data)

    def build_ranking(self):
        """
        This method is used to sort the data within the file that contains the progress of
        players in order to create a ranking.
        :return: This method does not return something.
        """
        data = self.read_lines()
        data_list = [elem.split(',') for elem in data]
        data_list = [[elem.strip() for elem in sublist] for sublist in data_list]

        sorted_list = sorted(data_list, key=lambda x: int(x[1].strip()), reverse=True)

        ranked_list = [', '.join(elem for elem in sublist) for sublist in sorted_list]
        data = ' \n'.join(elem for elem in ranked_list) + '\n'
        self.write_file(data)
