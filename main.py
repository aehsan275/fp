from Trie import Trie

def main():
    trie = Trie("words.txt")
    print(trie.is_valid_word("AA"))
    print(trie.get_valid_words("AA"))


if __name__ == "__main__":
    main()