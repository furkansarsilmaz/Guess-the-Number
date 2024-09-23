from tkinter import *

def guess_great(self):
    """
    window for when entry is greater than number
    """
    self.clear_screen()
    self.great_guess_label = Label(self.root,text="Number is lower\nthan your guess",font=("arial",14,"bold italic"))
    self.great_guess_label.pack()
    self.text_guess = Text(self.root,width=11,height=1)
    self.text_guess.pack()
    
    self.button_enter = Button(self.root,text="Enter",width=3,height=2,command=self.enter_number)
    self.button_enter.pack()
    
    self.Button_Exit = Button(self.root,text="Exit",width=3,height=2,command=lambda:self.root.quit())
    self.Button_Exit.pack()