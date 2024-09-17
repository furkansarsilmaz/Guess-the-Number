from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import time
import random

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
        self.play_menu()

    def play_menu(self):
        self.clear_screen()
        self.retained_number = random.randint(0,9)
        self.label_start = Label(self.root,text="Guess the number\nIm holding ?",font=("arial",14,"bold italic")).pack()
        
        self.text_guess = Text(self.root,width=11,height=1)
        self.text_guess.pack()
        
        self.button_enter = Button(self.root,text="Enter",width=3,height=2,command=self.enter_number)
        self.button_enter.pack()
        
        self.Button_Exit = Button(self.root,text="Exit",width=3,height=2,command=lambda:self.root.quit())
        self.Button_Exit.pack()

    def enter_number(self):        
        try :
            number = self.text_guess.get("1.0",END)
            number = number.strip()

            if self.try_chance == 0 :
                messagebox.showerror("Lose","You lose...")
                self.root.destroy()
                return            

            if self.retained_number == int(number) :
                self.win_screen()

            elif self.retained_number < int(number):
                self.guess_great()
                self.try_chance -= 1
            
            elif self.retained_number > int(number):
                self.guess_low()
                self.try_chance -= 1

        except ValueError :
            messagebox.showerror("Error","Enter a valid number")
            self.try_chance -= 1

    def win_screen(self):
        self.clear_screen()
        self.label_retry = Label(self.root,text="You won !!\n Do you wanna play again ? ",font=("arial",14,"bold italic"))
        self.label_retry.pack()

        self.button_yes = Button(self.root,text="Yes",width=3,height=2,command=self.play_menu)
        self.button_yes.pack()

        self.button_no = Button(self.root,text="No",width=3,height=2,command=lambda:self.root.quit())
        self.button_no.pack()

    def clear_screen(self):
        for i in self.root.winfo_children():
            i.destroy()
    
    def guess_low(self):
        self.clear_screen()

        self.low_guess_label = Label(self.root,text="Number is greater\nthan your guess",font=("arial",14,"bold italic"))
        self.low_guess_label.pack()

        self.text_guess = Text(self.root,width=11,height=1)
        self.text_guess.pack()
        
        self.button_enter = Button(self.root,text="Enter",width=3,height=2,command=self.enter_number)
        self.button_enter.pack()
        
        self.Button_Exit = Button(self.root,text="Exit",width=3,height=2,command=lambda:self.root.quit())
        self.Button_Exit.pack()

    def guess_great(self):
        self.clear_screen()

        self.great_guess_label = Label(self.root,text="Number is lower\nthan your guess",font=("arial",14,"bold italic"))
        self.great_guess_label.pack()

        self.text_guess = Text(self.root,width=11,height=1)
        self.text_guess.pack()
        
        self.button_enter = Button(self.root,text="Enter",width=3,height=2,command=self.enter_number)
        self.button_enter.pack()
        
        self.Button_Exit = Button(self.root,text="Exit",width=3,height=2,command=lambda:self.root.quit())
        self.Button_Exit.pack()

if __name__ == "__main__":
    root = Tk()
    Guess(root)
    root.mainloop()