import random

class Board:
    """
        Keeps track of pieces on the board.

        Stereotype: Information Holder

        Attributes: 
            _piles - List - Holds the number of Os in each row.
        
        Methods:
            __create_combination    Generates a random, 4 digit number.
            to_string               Converts the board data to a print()-able format.
            apply                   Removes Os from the play board according to user input
            is_empty                Returns `True` if the board (i.e _piles) contains only zeroes.
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
        guess = guess.strip('')
        correctness = ''
        for i in range(len(guess)):
            if guess[i] in self._combination:
                if i == self._combination[i]:
                    correctness += 'x'
                else:
                    correctness += 'o'
            else:
                correctness += '*'

    def numberGuessed(self):
        return False
            

Board()
Board.apply(0, '5555')