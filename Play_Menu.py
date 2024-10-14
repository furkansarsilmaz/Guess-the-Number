from tkinter import *
import random

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