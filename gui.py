import os
from tkinter import *

def p_color(color):
    os.system("cls")
    print(color)

def quit_game():
    quit()

color_gray = "#2b2b34"
color_green = "#18d770"
color_red = "#fb4c31"
color_blue = "#24a1e1"
color_yellow = "#efd82a"


window = Tk()
window.title("SIMON Game")
window.geometry("300x300")
window.configure(bg=color_gray)

frame = Frame(window, background="#FFFFFF",
                        width=250,
                        height=250)

sizeX = 50
sizeY = 40

button_green = Button(frame, bg=color_green, 
                        padx=sizeX, pady=sizeY,
                        command= lambda: p_color("green"))
button_green.grid(row=0,column=0)

button_red = Button(frame, bg=color_red, 
                    padx=sizeX, pady=sizeY,
                    command= lambda: p_color("red"))
button_red.grid(row=0,column=1)

button_yellow = Button(frame, bg=color_yellow, 
                        padx=sizeX, pady=sizeY,
                        command= lambda: p_color("yellow"))
button_yellow.grid(row=1,column=0)

button_blue = Button(frame, bg=color_blue, 
                        padx=sizeX, pady=sizeY,
                        command= lambda: p_color("blue"))

button_blue.grid(row=1,column=1)

frame.place(relx =.5, rely=.40, anchor=CENTER)

button_quit = Button(window, text="QUIT",
                        font=("Consolas", 15),
                        padx=30, pady=5,
                        command=quit_game)

button_quit.place(relx =.5, rely=.85, anchor=CENTER)

window.mainloop()