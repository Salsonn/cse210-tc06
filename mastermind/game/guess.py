class Guess:
    """The responsibility of Guess is to keep track of the mark found digits.
    
    Stereotype: 
        Information Holder

    Attributes:
        _number (integer): The opponents number to be referenced.
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._guess = guess

    def get_pile(self):
        """Returns the pile to remove from.

        Args:
            self (Move): an instance of Move.
        """
        return self._guess