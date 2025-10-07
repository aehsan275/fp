import os

class Board:

    def __init__(self, board=None, file=""):
        if os.path.splitext(file)[-1] == ".png":
            print("an image")
        elif os.path.splitext(file)[-1] == ".txt":
            print("text")
        elif file != "":
            print("invalid file")
        else:
            print("board")
