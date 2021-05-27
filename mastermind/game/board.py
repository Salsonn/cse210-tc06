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
        guess = str(guess.get_pile())
        guess = guess.strip('')
        self.combo_guess = ''
        self.correctness = ''

        for i in self._combination:
            self.combo_guess += f'{i}'

        for i in range(len(guess)):
            if guess[i] in self.combo_guess:
                if str(self._combination[i]) == guess[i]:
                    self.correctness += 'x'
                else:
                    self.correctness += 'o'
            else:
                self.correctness += '*'
        return self.correctness
    
    def is_empty(self):
        print(self.correctness)
        if self.correctness == 'xxxx':
            return True
        else:
            return False

Board()
