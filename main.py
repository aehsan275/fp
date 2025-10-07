from Trie import Trie

def main():
    trie = Trie("words.txt")
    print(trie.is_valid_word("AA"))
    trie.__dfs(1,1)


if __name__ == "__main__":
    main()