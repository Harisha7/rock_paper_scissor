# Import Required Library
from tkinter import *
import random
 
# Create Object
root = Tk()
 
# Set geometry
root.geometry("300x300")
 
# Set title
root.title("Rock Paper Scissor Game")
 

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


# Execute Tkinter
root.mainloop()		
 