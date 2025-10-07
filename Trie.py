class TrieNode:
    def __init__(self):
        self.__children = [None] * 26
        self.__end_of_word = False

    def get_children(self):
        return self.__children
    
    def set_children(self, index, value):
        self.__children[index] = value

    def get_end_of_word(self):
        return self.__end_of_word
    
    def set_end_of_word(self, value):
        self.__end_of_word = value



class Trie:

    def __init__(self, filename):
        self.__root = TrieNode()

        with open(filename, "r") as f:
            words = f.read().split("\n")
        for word in words:
            self.insert_word(word)
        

    def insert_word(self, word):
        current = self.__root # start at the root
        for character in word: # go through every character in the word
            index = ord(character) - 65 # 65 is the ASCII for 'A', so subtracting gives the index of the character in the alphabet
            if current.get_children()[index] is None: # if next node does not exist
                current.set_children(index, TrieNode()) # initialize next node
            current = current.get_children()[index] # move to next node
        current.set_end_of_word(True)# the word has now ended

    def is_valid_word(self, word):
        current = self.__root
        for character in word:
            index = ord(character) - 65
            if current.get_children()[index] is None:
                return False
            current = current.get_children()[index]
        return current.get_end_of_word()
    
    def get_valid_words(self, prefix):
        start = self.__root
        for character in prefix:
            index = ord(character) - 65
            if start.get_children()[index] is None:
                return []
            start = start.get_children()[index]
        
        words = self.__dfs(start, prefix)
        return words

    def __dfs(self, current_node, current_word): # using dfs to traverse through trie to get valid words
        
        words = []
        if current_node.get_end_of_word():
            words.append(current_word)
        
        for index,child in enumerate(current_node.get_children()):
            if child is not None:
                words.extend(self.__dfs(current_node.get_children()[index], current_word + chr(index + 65)))

        return words
        