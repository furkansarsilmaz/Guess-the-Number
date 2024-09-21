from tkinter import *
from Play_Menu import play_menu

def win_screen(self):
    self.clear_screen()
    self.label_retry = Label(self.root,text="You won !!\n Do you wanna play again ? ",font=("arial",14,"bold italic"))
    self.label_retry.pack()
    self.button_yes = Button(self.root,text="Yes",width=3,height=2,command=self.play)
    self.button_yes.pack()
    self.button_no = Button(self.root,text="No",width=3,height=2,command=lambda:self.root.quit())
    self.button_no.pack()