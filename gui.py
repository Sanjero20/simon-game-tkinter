import os, random, time

from tkinter import *
import pygame

from button_class import Color_Button

#Color codes
BACKGROUND = "#2b2b34"

GREEN = ("#18d770", "beep_green.ogg")
RED = ("#fb4c31", "beep_red.ogg")
YELLOW = ("#efd82a", "beep_yellow.ogg")
BLUE = ("#24a1e1", "beep_blue.ogg")

myfont = ("Consolas", 15)

#Initiate pymixer
pygame.mixer.init()

class Simon:
    def __init__(self):
        # self.game_state = "watch"
        self.choices = ['R', 'G', 'B', 'Y']
        self.pattern = []

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
        self.Button_GREEN = Color_Button()
        self.Button_RED = Color_Button()
        self.Button_YELLOW = Color_Button()
        self.Button_BLUE = Color_Button()

        # Set Button Color and Sounds
        self.Button_GREEN.set_properties(GREEN[0], GREEN[1], "G")
        self.Button_RED.set_properties(RED[0], RED[1], "R")
        self.Button_YELLOW.set_properties(YELLOW[0], YELLOW[1], "Y")
        self.Button_BLUE.set_properties(BLUE[0], BLUE[1], "B")

        #Place button in Frame in grid manner
        self.Button_GREEN.place_Button(self.frame_Game, 0, 0)
        self.Button_RED.place_Button(self.frame_Game, 0, 1)
        self.Button_YELLOW.place_Button(self.frame_Game, 1, 0)
        self.Button_BLUE.place_Button(self.frame_Game, 1, 1)

        # From Game menu return to main menu
        self.Button_MENU = Button(self.frame_Combined,
                                    text="MENU", font=myfont,
                                    command=self.play_pattern
                                    )

    def show_widget(self, widget, x=0, y=0, side=TOP):
        """Show widget to the self.window"""
        widget.pack(padx=x, pady=y, side=side)

    def hide_widget(self, widget):
        """Hide Widget that uses the .pack() method"""
        widget.pack_forget()

    def goto_gamebackground(self):
        """Destroy Main Menu proceed to Game"""
        self.hide_widget(self.frame_Menu)
        self.game_background()

    def return_menu(self):
        self.hide_widget(self.Button_MENU)
        self.hide_widget(self.frame_Combined)
        self.main_menu()
        
    def main_menu(self):
        self.show_widget(self.frame_Menu)
        self.button_START = Button(self.frame_Menu,
                                    text="START", font=myfont,
                                    padx=15, 
                                    command=self.goto_gamebackground
                                    )
        self.button_QUIT = Button(self.frame_Menu,
                                    text="QUIT", font=myfont,
                                    padx=18, 
                                    command=quit
                                    )

        self.button_START.place(relx=0.5, rely=0.41, anchor=CENTER)
        self.button_QUIT.place(relx=0.5, rely=0.56, anchor=CENTER)

    def game_background(self):
        """Show Game"""
        self.show_widget(self.frame_Combined, 0, 20)
        self.show_widget(self.frame_Game)

        self.init_Buttons()
        self.show_widget(self.Button_MENU, 0, 10, side=LEFT)

    def start_game(self):
        pass
        
    def add_pattern(self):
        """Add a random pattern into the list."""
        self.pattern.append(random.choice(self.choices))

    def play_pattern(self):
        """Play the pattern thru demonstation"""
        for i in self.choices:
            if i == 'R':
                self.Button_RED.flash()
            elif i == 'G':
                self.Button_GREEN.flash()
            elif i == 'B':
                self.Button_BLUE.flash()
            elif i == 'Y':
                self.Button_YELLOW.flash()

            time.sleep(0.75)
    
    def game_status(self):
        if game_state == "watch":
            # Play pattern sequence
            pass
        else:
            # Verify player turn sequence
            pass

simon = Simon()