from Logic import Logic

def main():
    logic = Logic("words.txt")
    logic.read_words()
    print(logic.dictionary)

if __name__ == "__main__":
    main()