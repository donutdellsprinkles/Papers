from tkinter import *
from random import randrange

# 0 = rock
# 1 = paper
# 2 = scissors
computer_choice = randrange(0, 3)


def rock():
    if computer_choice == 0:
        Label(text="Tie").pack()
    elif computer_choice == 1:
        Label(text="Lost").pack()
    else:
        Label(text="Won!").pack()


def paper():
    if computer_choice == 1:
        Label(text="Tie").pack()
    elif computer_choice == 2:
        Label(text="Lost").pack()
    else:
        Label(text="Won!").pack()


def scissors():
    if computer_choice == 2:
        Label(text="Tie").pack()
    elif computer_choice == 0:
        Label(text="Lost").pack()
    else:
        Label(text="Won!").pack()


window = Tk()

Button(text="Rock", command=rock).pack()
Button(text="Paper", command=paper).pack()
Button(text="Scissors", command=scissors).pack()

window.mainloop()
