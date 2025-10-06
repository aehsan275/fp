class Dictionary:

    def __init__(self, words_file):
        self.words_file = words_file
        self.dictionary = set()

    def read_words(self):
        with open(self.words_file, "r") as f:
            self.dictionary = f.read().split("\n")
