from tkinter import simpledialog, PhotoImage, Frame
from network import connect, send
from tkinter import *
#import random
from style import set_style
from tk_sleep import tk_sleep


# Create Object
window = Tk()
 
# Set geometry
window.geometry("1000x1000")
set_style(window)

# Set title
window.title("Rock Paper Scissor Game")

game_state = {
    'me': None,
    'opponent': None,
    'is_server': None,
    'shared': None,
		'my_score' : 0,
		'opponent_score' : 0
}


# Reset The Game
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Player              ")
    l3.config(text = "Opponent")
    l4.config(text = "")
 
# Disable the Button
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

# If player selected rock
def isrock():
    button_disable()
 
# If player selected paper
def ispaper():
    button_disable()
 
# If player selected scissor
def isscissor():
    button_disable()
 
#def draw_board():
# Add Labels, Frames and Button
Label(window,
			text = "Rock Paper Scissor",
			font = "normal 20 bold",
			fg = "blue").pack(pady = 20)

frame = Frame(window)
frame.pack()

l1 = Label(frame,
					text = "Player              ",
					font = 10)

l2 = Label(frame,
					text = "VS             ",
					font = "normal 10 bold")

l3 = Label(frame, text = "Opponent", font = 10)

l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()


"""my_score = Label(window,
					text = "My Score",
					font = "normal 20 bold",
					bg = "white",
					width = 3 ,
					borderwidth = 2,
					relief = "solid")

my_score.pack(padx=20)

opponent_score = Label(window,
					text = "Opponent Score",
					font = "normal 20 bold",
					bg = "white",
					width = 3 ,
					borderwidth = 2,
					relief = "solid")
opponent_score.pack(padx=40)"""

l4 = Label(window,
					text = "",
					font = "normal 20 bold",
					bg = "white",
					width = 15 ,
					borderwidth = 2,
					relief = "solid")
l4.pack(pady = 20)

frame1 = Frame(window)
frame1.pack()

b1 = Button(frame1, text = "Rock",
#            image = ''
						font = 10, width = 7,
						command = isrock)

b2 = Button(frame1, text = "Paper ",
						font = 10, width = 7,
						command = ispaper)

b3 = Button(frame1, text = "Scissor",
						font = 10, width = 7,
						command = isscissor)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)

Button(window, text = "Reset Game",
			font = 10, fg = "red",
			bg = "black", command = reset_game).pack(pady = 20)

window.mainloop()		
