import sys
from random import randint
from tkinter import simpledialog, PhotoImage, Frame
from network import connect, send, close
from tkinter import *
from tk_sleep import tk_sleep


# Create Object
window = Tk()

# Set geometry
window.geometry("500x500")
game_exit = False

#closing event handler
def on_closing():
    close()
    window.destroy()
    game_exit = True

window.protocol("WM_DELETE_WINDOW", on_closing)

# Set title
window.title("Rock Paper Scissor Game")

game_state = {
    'me': None,
    'opponent': None,
    'my_selection' : None,
    'opponent_selection' : None
}

result_validation = [
    ['Rock', 'Paper', 'opponent'],
    ['Paper', 'Rock', 'me'],
    ['Scissor', 'Rock', 'opponent'],
    ['Rock', 'Scissor', 'me'],
    ['Paper', 'Scissor', 'opponent'],
    ['Scissor', 'Paper', 'me']
]

def evaluate_result():
    if game_state['my_selection'] and game_state['opponent_selection']:
        l1.config(text = game_state['my_selection'] + "         ")
        l3.config(text = game_state['opponent_selection'])
        if game_state['my_selection'] == game_state['opponent_selection']:
            l4.config(text = "Match  Drawn")
        else:
            for x in result_validation:
                if x[0] == game_state['my_selection'] and x[1] == game_state['opponent_selection']:
                    l4.config(text = game_state[x[2]] + " Won")

# Reset The Game
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Player              ")
    l3.config(text = "Opponent")
    l4.config(text = "")
    game_state['my_selection'] = None
    game_state['opponent_selection'] = None
    l4.config(text = game_state['opponent'] + " connected")

# Disable the Button
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

# If player selected rock
def isrock():
    game_state['my_selection'] = 'Rock'
    send('Rock')
    evaluate_result()
    button_disable()
 
# If player selected paper
def ispaper():
    game_state['my_selection'] = 'Paper'
    send('Paper')
    evaluate_result()
    button_disable()
 
# If player selected scissor
def isscissor():
    game_state['my_selection'] = 'Scissor'
    send('Scissor')
    evaluate_result()
    button_disable()
 
#def draw_board():
# Add Labels, Frames and Button
Label(window,
      text = "Rock Paper Scissor",
      font = "normal 20 bold",
      fg = "blue").pack(pady = 20)

frame = Frame(window)
frame.pack()

l0 = Label(window,
            text = "",
            font = "normal 20 bold",
            bg = "green",
            width = 15 ,
            borderwidth = 2,
            relief = "solid")
l0.pack(pady = 20)

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
            font = 10, width = 7,
            command = isrock)

b2 = Button(frame1, text = "Paper",
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

def get_opponent_and_decide_game_runner(user, message):
    # who is the server (= the creator of the channel)
    if 'created the channel' in message:
        name = message.split("'")[1]
    # who is the opponent (= the one that joined that is not me)
    if 'joined channel' in message:
        name = message.split(' ')[1]
        if name != game_state['me']:
            game_state['opponent'] = name

def message_handler(timestamp, user, message):
    if user == 'system': 
        get_opponent_and_decide_game_runner(user, message)

    if user == game_state['opponent'] and type(message) is str:
        game_state['opponent_selection'] = message
        evaluate_result()

# start - before game loop
def start():
    l4.config(text = "Not Connected")
    # connect to network
    game_state['me'] = simpledialog.askstring(
            'Input', 'Your user name', parent=window)
    channel = simpledialog.askstring(
            'Input', 'Channel', parent=window)
    connect(channel, game_state['me'], message_handler)
    l0.config(text = game_state['me'])
    # wait for an opponent 
    while game_state['opponent'] == None and game_exit == False:
        tk_sleep(window, 1 / 10)
    l4.config(text = game_state['opponent'] + " connected")

# Execute Tkinter
start()
window.mainloop()
