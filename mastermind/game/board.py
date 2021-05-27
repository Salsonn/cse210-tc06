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
        self.is_correct('1234')

    def __create_combination(self):
        combo = []
        for _ in range(4):
            combo.append(random.randint(1, 9))
        return combo
    
    def to_string(self):
        pass

    def apply(self, guess):
        guess = guess.strip('')
        combo_guess = ''
        correctness = ''
        
        for i in self._combination:
            combo_guess += f'{i}'

        for i in range(len(guess)):
            if guess[i] in combo_guess:
                if str(self._combination[i]) == guess[i]:
                    correctness += 'x'
                else:
                    correctness += 'o'
            else:
                correctness += '*'
        return correctness

Board()
