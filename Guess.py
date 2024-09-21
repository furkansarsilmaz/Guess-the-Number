from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import time
import random
from Win_Screen import win_screen
from Play_Menu import play_menu
from Guess_Low import guess_low
from Guess_Great import guess_great

class Guess:
    def __init__(self,root):
        self.root = root
        self.root.geometry("300x200")
        self.root.title("Guess ??")

        self.Label_Menu = Label(self.root,text="Welcome to the game",font=("Arial",14,"bold italic")).pack(pady=20)

        self.Button_Play = Button(self.root,text="Play",width=3,height=2,command=self.play).pack(pady=10)
        self.Button_Exit = Button(self.root,text="Exit",width=3,height=2,command=lambda:self.root.quit()).pack()
        self.try_chance = 3

    def update_menu(self):
        for i in self.root.winfo_children():
            i.destroy()

    def play(self):
        self.update_menu()
        time.sleep(1)
        play_menu(self)

    def enter_number(self):        
        try :
            number = self.text_guess.get("1.0",END)
            number = number.strip()

            if self.try_chance == 0 :
                messagebox.showerror("Lose","You lose...")
                self.root.destroy()
                return            

            if self.retained_number == int(number) :
                win_screen(self)

            elif self.retained_number < int(number):
                guess_great(self)
                self.try_chance -= 1
            
            elif self.retained_number > int(number):
                guess_low(self)
                self.try_chance -= 1

        except ValueError :
            messagebox.showerror("Error","Enter a valid number")
            self.try_chance -= 1

    def clear_screen(self):
        for i in self.root.winfo_children():
            i.destroy()
    
if __name__ == "__main__":
    root = Tk()
    Guess(root)
    root.mainloop()