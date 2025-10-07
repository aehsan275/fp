class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

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
            if current.children[index] is None: # if next node does not exist
                current.children[index] = TrieNode() # initialize next node
            current = current.children[index] # move to next node
        current.endOfWord = True # the word has now ended

    def is_valid_word(self, word):
        current = self.__root
        for character in word:
            index = ord(character) - 65
            if current.children[index] is None:
                return False
            current = current.children[index]
        return current.endOfWord
    
    def get_valid_words(self, prefix):
        start = self.__root
        for character in prefix:
            index = ord(character) - 65
            if start.children[index] is None:
                return []
            start = start.children[index]
        
        words = self.dfs(start, prefix)
        return words

    def __dfs(self, current_node, current_word): # using dfs to traverse through trie to get valid words
        
        words = []
        if current_node.endOfWord:
            words.append(current_word)
        
        for index,child in enumerate(current_node.children):
            if child is not None:
                words.extend(self.__dfs(current_node.children[index], current_word + chr(index + 65)))

        return words
        