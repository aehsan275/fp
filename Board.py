import os
import requests

class Board:

    def __init__(self, board_string=None, file=""):
        if os.path.splitext(file)[-1] == ".jpg":
            self.board = self.__get_board_from_image(file)
            print(self.board)
        elif os.path.splitext(file)[-1] == ".txt":
            self.board = self.__get_board_from_text(file)
            print(self.board)
        elif file != "":
            print("invalid file")
        else:
            self.board = [line.split(",") for line in board_string.split("|")]
            print(self.board)

    def __get_board_from_image(self, filename):
        files = {"file": open(filename, "rb")}
        response = requests.post('https://scrabblecam.com/process', files=files)

        if response.json()["status"] == "OK":
            print(response.json())
            return [line.split(",") for line in response.json()["board"].split("|")]
        else:
            return None
        
    def __get_board_from_text(self, filename):
        with open(filename, "r") as f:
            return [line.split(",") for line in f.read().split("|")]

