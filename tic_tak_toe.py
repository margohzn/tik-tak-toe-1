from tkinter import * 
import random
from tkinter import messagebox

class Tik_tak_toe:

    def __init__(self, window, mode):
        pass

class Menu:
    
    def __init__(self, window):
        self.window = window
        self.window.title("Tic Tak Toe starting page")
        self.create_widjts()
        
    def create_widjts(self):
        title = Label(self.window, text = "Select Mode", font = ("normal", 20)).pack(pady = 15, padx = 15)
        button1 = Button(self.window, text = "Single Player", font = ("times", 15), command = self.start_single_player).pack(pady = 15, padx = 15)
        button2 = Button(self.window, text = "Multi Player", font = ("times", 15), command = self.start_multi_player).pack(pady = 15, padx = 15)

    def start_single_player(self):
        self.window.destroy()
        self.start_game("single")

    def start_multi_player(self):
        self.window.destry()
        self.start_game("multi")

    def start_game(self, mode):
        window2 = Tk()
        Tik_tak_toe(window2, mode)
        window2.mainloop()


if __name__ == "__main__":
    window1 = Tk()
    Menu(window1)

