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
        self._piles = self.__create_piles()

    def __create_piles(self):
        pile_array = []
        for i in range(random.randint(2,5)):
            pile_array.append(random.randint(1,9))
        return pile_array
    
    def to_string(self):
        stringy_pile = "--------------------\n"
        for i in range(len(self._piles)):
            stringy_pile += (f"{str(i)}: ")
            for j in range(self._piles[i]):
                stringy_pile += 'O '
            stringy_pile += '\n'
        stringy_pile += "--------------------\n"
        return stringy_pile

    def apply(self, guess):
        guess = guess.get_pile()
        # self._piles[pile_num] = max(self._piles[pile_num] - stones, 0)
        return

    def is_empty(self):
        if all(i == 0 for i in self._piles):
            return True
