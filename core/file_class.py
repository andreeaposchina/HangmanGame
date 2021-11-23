from settings import *
from random import choice
from os import path


class File:
    def __init__(self, filename):
        self.filename = filename

    def read_lines(self) -> list:
        with open(self.filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        return lines

    def read_file(self) -> str:
        with open(self.filename, 'r') as file:
            data = file.read()
        return data

    def write_file(self, data) -> None:
        with open(self.filename, 'w') as file:
            file.write(data)

    def choose_word(self) -> str:
        lst = self.read_lines()
        return choice(lst)

    def build_history(self, data: str):
        if path.isfile(BASE_DIR_PATH + "\\" + self.filename):
            existing_data = self.read_file()
            data = existing_data + data
            self.write_file(data)
        else:
            self.write_file(data)

    def build_ranking(self):
        data = self.read_lines()
        data_list = [elem.split(',') for elem in data]
        data_list = [[elem.strip() for elem in sublist] for sublist in data_list]

        sorted_list = sorted(data_list, key=lambda x: int(x[1].strip()), reverse=True)

        ranked_list = [', '.join(elem for elem in sublist) for sublist in sorted_list]
        data = ' \n'.join(elem for elem in ranked_list) + '\n'
        self.write_file(data)
