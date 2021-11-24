from core.settings import *


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_lines(self) -> list:
        """
        This method is used to read the content of a file by lines.
        :return: A list of lists that contains the lines of the file
        """
        with open(BASE_DIR_PATH + '\\' + self.filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]

        return lines

    def read_file(self) -> str:
        """
        This method is used to read the content of a file.
        :return: A string that contains the content of the file
        """
        with open(BASE_DIR_PATH + '\\' + self.filename, 'r') as file:
            data = file.read()
        return data

    def write_file(self, data: str) -> None:
        """
        This method is used to write data into a file.
        :param data: Must be a string
        :return: This method does not return something.
        """
        with open(BASE_DIR_PATH + '\\' + self.filename, 'w') as file:
            file.write(data)
