import random

class Board:
    """
        Keeps track of pieces on the board.

        Stereotype: Information Holder

        Attributes: 
            _piles - List - Holds the number of Os in each row.
        
        Methods:
            __create_piles      Generates random board size and values.
            to_string           Converts the board data to a print()-able format.
            apply               Removes Os from the play board according to user input
            is_empty            Returns `True` if the board (i.e _piles) contains only zeroes.
    """
    def __init__(self):
        self._guess = self.__create_()

    def to_string(self):
        text = '\n--------------------'
        for guess, secret in enumerate(self._guess):
            #text += (f'\n{guess}: ' + 'O ' * secret)
            if guess.index() == secret.index():
                text += 'X'
            elif guess.index() != secret.index():
                text += 'O'
            else:
                text += '*'
        text += '\n--------------------'
        return text

    def is_empty(self):
        if all(i == 0 for i in self._guess):
            return True
