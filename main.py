from Dictionary import Dictionary
from Trie import Trie

def main():
    dictionary = Dictionary("words.txt")
    dictionary.read_words()
    trie = Trie(dictionary.dictionary)
    trie.insert_dictionary()
    print(trie.is_valid("AALSSFDSFSDFASD"))


if __name__ == "__main__":
    main()