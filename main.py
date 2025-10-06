from Dictionary import Dictionary
from Trie import Trie

def main():
    dictionary = Dictionary("words.txt")
    dictionary.read_words()
    print(dictionary.dictionary)
    trie = Trie(dictionary.dictionary)
    trie.insert_dictionary()


if __name__ == "__main__":
    main()