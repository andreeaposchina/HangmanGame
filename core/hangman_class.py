from core.history_class import History
from datetime import datetime


class Hangman:
    def __init__(self):
        self.words_file_instance = History("words_file.txt")
        self.history_file_instance = History("history_points.txt")
        self.word = self.words_file_instance.choose_word()
        self.name = ''
        self.no_points = 0
        self.no_lives = 6
        self.guessed_word = '_' * len(self.word)

        self.start = input("Do you want to play Hangman? \n"
                           "Please press Y and ENTER if you want to play or N and ENTER if you want to exit: ")
        while self.start.lower() not in ['y', 'n']:
            self.start = input("Wrong command. "
                               "Please press Y and ENTER if you want to play or N and ENTER if you want to exit: ")

    def _start_game(self):
        """
        This method contains the main algorithm of the Hangman game.
        :return: This method does not return something.
        """
        self.name = input("Please enter your name or nickname: ").upper()
        guessed_letters = []
        given_word_list = [letter for letter in self.word]
        guessed_word_list = [char for char in self.guessed_word]

        while self.guessed_word != self.word and self.no_lives != 0:
            letter = input("Please pick a letter: ")
            if letter in guessed_letters:
                print("You already guessed this letter")
                continue
            else:
                guessed_letters.append(letter)
                if letter in self.word:

                    for i in range(len(given_word_list)):
                        if letter == self.word[i]:
                            guessed_word_list[i] = letter
                else:
                    print("Oops! This letter is not in the word")
                    self.no_lives -= 1
            self.guessed_word = ''.join(guessed_word_list)
            if self.no_lives != 0:
                print(f"The word is now: {self.guessed_word}")
                print(f"You have {self.no_lives} more lives")

    @staticmethod
    def _exit_game():
        """
        This method is used to exit the game if the user does not want to play.
        :return: This method does not return something.
        """
        print("Ok, bye :(")
        exit()

    def _calculate_points(self):
        """
        This method is used to compute the total number of points.
        The final number of points depends on the length of the word and on the number of lives that remained.
        :return: This method does not return something
        """
        self.no_points = 100 * self.no_lives * len(self.word)

    def _show_results(self):
        """
        This method is always returned at the end of a game. It prints a summary of the game.
        :return: This method does not return something
        """
        if self.no_lives == 0:
            print(f"Game over, {self.name}! :( The word was {self.word} \n "
                  f"You obtained {self.no_points} points \n Better luck next time!")
        else:
            print(f"Congratulations, {self.name}! :) You obtained {self.no_points} points")

    def _add_user_to_history(self):
        """
        This method is used to record the points, the user and the date and time when the user got the score.
        :return: This method does not return something
        """
        data = f"{self.name}, {self.no_points}, {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} \n"
        self.history_file_instance.build_history(data)

    # def _print_ranking(self):
    #     """
    #     This method is always returned at the end of a game. It prints the history of plays by making a ranking.
    #     :return: This method does not return something
    #     """
    #     self.history_file_instance.build_ranking()
    #
    #     ranking = self.history_file_instance.read_lines()
    #     for line in ranking:
    #         print(line)

    def play_game(self):
        """
        This is the main method. It calls all methods from the class.
        :return: This method does not return something
        """
        if self.start.lower() == 'y':
            self._start_game()
        else:
            self._exit_game()

        self._calculate_points()
        self._add_user_to_history()
        self._show_results()
        self.history_file_instance.print_ranking()
