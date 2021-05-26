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
        self._combination = self.__create_combination()

    def __create_combination(self):
        combo = []
        for _ in range(4):
            combo.append(random.randint(1, 9))
        return combo
    
    def to_string(self):
        pass

    def apply(self, guess):
        guess = guess.get_pile()
        # self._piles[pile_num] = max(self._piles[pile_num] - stones, 0)
        return

    def is_empty(self):
        pass

Board()