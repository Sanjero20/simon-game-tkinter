import os, random, time, pygame
from tkinter import *

BACKGROUND = "#2b2b34"

GREEN = ("#18d770", "beep_green.ogg")
RED = ("#fb4c31", "beep_red.ogg")
YELLOW = ("#efd82a", "beep_yellow.ogg")
BLUE = ("#24a1e1", "beep_blue.ogg")

myfont = ("Consolas", 15)

#Initiate pymixer
pygame.mixer.init()

class Game():
    def __init__(self, mainframe, widget_frame):    
        self.window = mainframe
        self.frame_Game = widget_frame
        self.frame_Buttons = Frame(self.frame_Game, background=BACKGROUND)
    
        self.choices = ['R', 'G', 'B', 'Y']
        self.pattern = []
        self.currentSteps = 0
        self.currentClicked = ""

        # Game Stats
        self.game_state = StringVar()
        self.game_state.set("watch")  

        self.highscore = IntVar()
        self.highscore_txt = StringVar()
        self.highscore_txt.set(f"Highscore: {self.highscore.get()}")
        self.score = IntVar()
        self.score_txt = StringVar()
        self.score_txt.set(f"Score: {self.score.get()}")

        self.init_Buttons()
        self.frame_Buttons.pack()
        self.frame_Game.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Game Things that i dont know what to do 
        self.listofButtons = [self.Button_GREEN,
                              self.Button_RED,
                              self.Button_YELLOW,
                              self.Button_BLUE,
                              ]

        self.gameover = False

    def init_Buttons(self):
        """Initialize Buttons"""
        self.Button_GREEN = Button(self.frame_Buttons,
                                    bg=GREEN[0],
                                    padx=50, 
                                    pady=40,
                                    command=lambda: self.buttonClicked(GREEN[1], 'G'),
                                    )
        self.Button_RED = Button(self.frame_Buttons, 
                                    bg=RED[0],
                                    padx=50, 
                                    pady=40,
                                    command=lambda: self.buttonClicked(RED[1], 'R'),
                                    )
        self.Button_YELLOW = Button(self.frame_Buttons, 
                                    bg=YELLOW[0],
                                    padx=50, 
                                    pady=40,
                                    command=lambda: self.buttonClicked(YELLOW[1], 'Y'),
                                    )
        self.Button_BLUE = Button(self.frame_Buttons, 
                                    bg=BLUE[0],
                                    padx=50, 
                                    pady=40,
                                    command=lambda: self.buttonClicked(BLUE[1], 'B'),
                                    )
        
        # Places buttons in a grid manner
        self.Button_GREEN.grid(row=0, column=0)
        self.Button_RED.grid(row=0, column=1)
        self.Button_YELLOW.grid(row=1, column=0)
        self.Button_BLUE.grid(row=1, column=1)

        self.Button_PLAY = Button(self.frame_Game,
                                    text="play", font=myfont,
                                    command=self.startGame
                                    )

        self.Button_PLAY.place(relx=0.5,rely=0.5, anchor=CENTER)

    def playSound(self, soundFile):
        pygame.mixer.music.load(f"audio\\{soundFile}")
        pygame.mixer.music.play()

    def buttonClicked(self, soundFile, color_code):
        """Will trigger if any of the 4 colored buttons is pressed"""

        if not self.gameover:
            self.playSound(soundFile)

        if self.game_state.get() == "your turn":
            self.currentClicked = color_code

            # Check if the player pressed the correct button
            if self.currentClicked == self.pattern[self.currentSteps]:
                self.currentSteps += 1

                # If Player clicked the correct button, check if it is the last part of the pattern
                # Proceeds to a new round, add score 
                if self.currentSteps == len(self.pattern):
                    self.currentSteps = 0
                    self.frame_Buttons.update()     # updates the frame buttons so no lag
                    time.sleep(1)
                    self.add_score()
                    self.next_round()

            # If Player guessed wrong, disable all the playable button   
            else: 
                self.playSound("gameover.ogg")

                self.Button_PLAY["text"] = "PLAY"
                self.Button_PLAY["state"] = NORMAL

                self.game_state.set("YOU LOSE")
                self.label_state.update()

                for i in self.listofButtons:
                    self.adjustButtons(i, relief=SUNKEN, state=DISABLED)

                for i in self.listofButtons:
                    self.adjustcolor(i, 'gray')

                self.set_highscore()

    def adjustButtons(self, button, relief=RAISED, state=NORMAL):
        """Adjust the button state and relief"""
        button['state'] = state
        button['relief'] = relief

    def adjustcolor(self, button, color):
        """Adjust the color of the button"""
        button['bg'] = color

    def get_highscore(self):
        """
        Retrieve previous highscore from txt file, 
        if not found, create a file and set highscore to zero
        """
        try:
            file = open("highscore.txt")
        except FileNotFoundError:
            file = open("highscore.txt", "w")
            file.write("0")
        else:
            highscore = file.read()
            if highscore:
                self.highscore.set(int(highscore))
            file.close()

        self.highscore_txt.set(f"Highscore: {self.highscore.get()}")

    def set_highscore(self):
        """Check if the score is higher than the highscore"""
        if self.score.get() > self.highscore.get():
            self.highscore.set(self.score.get())
            self.highscore_txt.set(f"Highscore: {self.highscore.get()}")
            self.window.update()

        with open("highscore.txt", "w") as file:
            file.write(str(self.highscore.get()))

    def display_gameState(self):
        """Shows the State of the game (watch / your turn)"""
        self.label_state = Label(self.window, textvariable=self.game_state, font=myfont)
        self.label_state.place(relx=0.5,rely=0.14, anchor=CENTER)

    def display_Score(self):
        """Shows the score and highscore on the window"""
        self.label_Score = Label(self.window, textvariable=self.score_txt, font=myfont)
        self.label_Score.place(x=20, y=300)

        self.label_Highscore = Label(self.window, textvariable=self.highscore_txt, font=myfont)
        self.label_Highscore.place(x=175, y=300)

    def add_pattern(self):
        """Add a random pattern into the list."""
        self.pattern.append(random.choice(self.choices))

    def play_pattern(self):
        """Play the pattern thru flashing animation"""
        self.game_state.set("watch")
        self.label_state.update()

        for i in self.pattern:
            if i == 'R':
                self.playSound(RED[1])
                self.Button_RED.flash()
            elif i == 'G':
                self.playSound(GREEN[1])
                self.Button_GREEN.flash()
            elif i == 'B':
                self.playSound(BLUE[1])
                self.Button_BLUE.flash()
            elif i == 'Y':
                self.playSound(YELLOW[1])
                self.Button_YELLOW.flash()

            time.sleep(0.75)

        self.game_state.set("your turn")
        self.label_state.update()

        self.waitingForInput = True

    def disable_playButton(self, text, state=DISABLED):
        """Changes the Play button to SIMON"""
        self.Button_PLAY['state'] = state
        self.Button_PLAY['text'] = text
        self.Button_PLAY['background'] = 'black'
        self.Button_PLAY['foreground'] = 'white'
        self.Button_PLAY.update()

    def add_score(self):
        """Add score"""
        score = self.score.get()
        self.score.set(score+1)
        self.score_txt.set(f"Score: {self.score.get()}")
   
    def reset_score(self):
        self.score.set(0)
        self.score_txt.set(f"Score: {self.score.get()}")

    def startGame(self):
        """When Play Button clicked, starts the game"""
        self.disable_playButton('SIMON')    # disable play button
        self.display_gameState()            # display gameState (watch/playerturn)
        self.display_Score()                # display scores
        time.sleep(0.5)

        self.get_highscore()
        self.restart()      # reset all stats
        self.next_round()
  
    def next_round(self):
        """
        Update the highscore everyround
        Add to pattern then show pattern sequence
        """
        self.set_highscore()
        self.add_pattern()
        self.play_pattern()

    def restart(self):
        """Reset all stats"""
        self.currentClicked = ""
        self.currentSteps = 0
        self.pattern.clear()
        self.reset_score()
        self.gameover = False

        for i in self.listofButtons:
            self.adjustButtons(i)

        self.adjustcolor(self.Button_GREEN, GREEN[0])
        self.adjustcolor(self.Button_RED, RED[0])
        self.adjustcolor(self.Button_YELLOW, YELLOW[0])
        self.adjustcolor(self.Button_BLUE, BLUE[0])