from tkinter import *
import pygame

pygame.mixer.init()

class ButtonSettings:
    """   """

    def playSound(self, soundFile):
        pygame.mixer.music.load(f"audio\\{soundFile}")
        pygame.mixer.music.play()

    def adjustButtons(self, button, relief=RAISED, state=NORMAL):
        """Adjust the button state and relief"""
        button['state'] = state
        button['relief'] = relief

    def adjustcolor(self, button, color):
        """Adjust the color of the button"""
        button['bg'] = color

    def disable_playButton(self, text, state=DISABLED):
        """Changes the Play button to SIMON"""
        self.Button_PLAY['state'] = state
        self.Button_PLAY['text'] = text
        self.Button_PLAY['background'] = 'black'
        self.Button_PLAY['foreground'] = 'white'
        self.Button_PLAY.update()
