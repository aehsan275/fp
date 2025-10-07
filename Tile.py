class Tile:

    __VALUES = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ': 0, '': 0}
    __letters_remaining = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, ' ': 2, '':226}

    def get_values(self):
        return self.__VALUES
    
    def get_letters_remaining(self):
        return self.__letters_remaining
     
    def __init__(self, letter, multiplier):
        self.letter = letter
        self.letter_value = self.__VALUES[letter]
        self.multiplier = multiplier
        self.__letters_remaining[letter] -= 1
        self.letter_score = self.letter_value * self.multiplier
        print(self.__letters_remaining)

        for letter,remaining in self.__letters_remaining.items():
            if remaining < 0:
                print("error")
                raise Exception(f"too many {letter} tiles used")
        
