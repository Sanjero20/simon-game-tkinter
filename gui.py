import os

from tkinter import *
import pygame

#Color codes
BACKGROUND = "#2b2b34"

GREEN = ("#18d770", "sound1_green.mp3")
RED = ("#fb4c31", "sound4_red.mp3")
BLUE = ("#24a1e1", "sound3_blue.mp3")
YELLOW = ("#efd82a", "sound2_yellow.mp3")

myfont = ("Consolas", 15)

#Initiate pymixer
pygame.mixer.init()

class Color_Button:
    """A Class that creates a button widget"""
    def __init__(self, color, sound):        
        self.color = color
        self.sound = sound

    def place_Button(self, frame, row, column):
        self.button = Button(frame, bg=self.color,
                                padx=50, pady=40,
                                command=self.play_sound)
        self.button.grid(row=row, column=column)

    def play_sound(self):
        pygame.mixer.music.load(f"audio\\{self.sound}")
        pygame.mixer.music.play()
        #Clear Terminal 
        os.system("CLS")

class Simon:
    def __init__(self):
        self.init_Window()
        self.main_menu()
        self.window.mainloop()
        
    def init_Window(self):
        """Initialize Windows"""
        self.window = Tk()
        self.window.title("SIMON Game")
        self.window.geometry("300x300")
        self.window.configure(bg=BACKGROUND)

        self.frame_Menu = Frame(self.window, background=BACKGROUND, width=300, height=300)
        self.frame_Combined = Frame(self.window, background=BACKGROUND, width=300, height=300)
        self.frame_Game = Frame(self.frame_Combined, background=BACKGROUND, width=300, height=300)
        
    def init_Buttons(self):
        """Initialize Buttons"""
        self.Button_GREEN = Color_Button(GREEN[0], GREEN[1])
        self.Button_RED = Color_Button(RED[0], RED[1])
        self.Button_BLUE = Color_Button(BLUE[0], BLUE[1])
        self.Button_YELLOW = Color_Button(YELLOW[0], YELLOW[1])
        #Place button in Frame in grid manner
        self.Button_GREEN.place_Button(self.frame_Game, 0, 0)
        self.Button_RED.place_Button(self.frame_Game, 0, 1)
        self.Button_BLUE.place_Button(self.frame_Game, 1, 1)
        self.Button_YELLOW.place_Button(self.frame_Game, 1, 0)

    def show_widget(self, widget, x=0, y=0):
        """Show widget to the self.window"""
        widget.pack(padx=x, pady=y)

    def hide_widget(self, widget):
        """Hide Widget that uses the .pack() method"""
        widget.pack_forget()

    def start(self):
        """Destroy Main Menu proceed to Game"""
        self.hide_widget(self.frame_Menu)
        self.game_menu()

    def return_menu(self):
        self.hide_widget(self.Button_MENU)
        self.hide_widget(self.frame_Combined)
        self.main_menu()
        
    def main_menu(self):
        self.show_widget(self.frame_Menu)
        self.button_START = Button(self.frame_Menu,
                                    text="START", font=myfont,
                                    padx=15, 
                                    command=self.start
                                    )
        self.button_QUIT = Button(self.frame_Menu,
                                    text="QUIT", font=myfont,
                                    padx=18, 
                                    command=quit
                                    )

        self.button_START.place(relx=0.5, rely=0.41, anchor=CENTER)
        self.button_QUIT.place(relx=0.5, rely=0.56, anchor=CENTER)

    def game_menu(self):
        """Show Game"""
        self.show_widget(self.frame_Combined, 0, 20)
        self.show_widget(self.frame_Game)
        self.init_Buttons()
        self.Button_MENU = Button(self.frame_Combined,
                                    text="MENU", font=myfont,
                                    command=self.return_menu
                                    )
        self.Button_MENU.pack(padx=0, pady=10, side=LEFT)

simon = Simon()