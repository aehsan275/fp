class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class Trie:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.root = TrieNode()

    def insert(self, word):
        current = self.root # start at the root
        for character in word: # go through every character in the word
            index = ord(character) - 65 # 65 is the ASCII for 'A', so subtracting gives the index of the character in the alphabet
            if current.children[index] is None: # if next node does not exist
                current.children[index] = TrieNode() # initialize next node
            current = current.children[index] # move to next node
        current.endOfWord = True # the word has now ended

    def insert_dictionary(self):
        for word in self.dictionary:
            self.insert(word)