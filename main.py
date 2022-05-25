from tkinter import *
import pygame

from game import Game

#Color codes
BACKGROUND = "#2b2b34"
myfont = ("Consolas", 15)

class GUI: 
    def __init__(self):
        self.init_Window()
        self.main_menu()
        self.window.mainloop()

    def init_Window(self):
        """Initialize Windows"""
        self.window = Tk()
        self.window.title("SIMON Game")
        self.window.geometry("350x350")
        self.window.resizable(False, False)

        icon = PhotoImage(file="image\\icon.png")
        self.window.iconphoto(True, icon)
        self.window.configure(bg=BACKGROUND)
        
        self.frame_Menu = Frame(self.window, background=BACKGROUND, width=300, height=300)
        self.frame_Game = Frame(self.window, background=BACKGROUND, width=300, height=300)
   
    def show_widget(self, widget, x=0, y=0, side=TOP):
        """Show widget to the self.window"""
        widget.pack(padx=x, pady=y, side=side)

    def hide_widget(self, widget):
        """Hide Widget that uses the .pack() method"""
        widget.pack_forget()

    def main_menu(self):
        self.show_widget(self.frame_Menu, x=0, y=20)
        self.button_START = Button(self.frame_Menu,
                                    text="START", font=myfont,
                                    padx=15, 
                                    command=self.goto_game
                                    )
        self.button_QUIT = Button(self.frame_Menu,
                                    text="QUIT", font=myfont,
                                    padx=18, 
                                    command=quit
                                    )

        self.button_START.place(relx=0.5, rely=0.41, anchor=CENTER)
        self.button_QUIT.place(relx=0.5, rely=0.56, anchor=CENTER)

    def goto_game(self):
        """Destroy Main Menu proceed to the Game"""
        self.hide_widget(self.frame_Menu)
        game = Game(self.window, self.frame_Game)

if __name__ == "__main__":
    play = GUI()