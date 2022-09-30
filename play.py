#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

from termcolor import colored
import random
import os

try: # Try to clear the terminal if not possible pass.
    os.system("cls||clear")  # Clear the terminal
except:
    pass

class colors:
    def __init__(self):
        self.FullBlock = "\u2588"  # Create a fullblock
        self.RED = colored(colors.FullBlock, "red")
        self.GREY = colored(colors.FullBlock, "grey")
        self.GREEN = colored(colors.FullBlock, "green")
        self.YELLOW = colored(colors.FullBlock, "yellow")
        self.BLUE = colored(colors.FullBlock, "blue")
        self.MAGENTA = colored(colors.FullBlock, "magenta")
        self.CYAN = colored(colors.FullBlock, "cyan")
        self.WHITE = colored(colors.FullBlock, "white")


    def computerChoice(self):
        self.count = 0
        self.CPU = []
        while copmputerChoice.count != 4:
            computerChoice.count += 1
            self.ALL = [colors.RED, colors.GREY, colors.GREEN, colors.YELLOW, colors.BLUE, colors.MAGENTA, colors.CYAN, colors,WHITE]
            random.shuffle(computerChoice.ALL)
            computerChoice.CPU.append(computerChoiceALL[0])

        return(computerChoice.CPU)

game = colors()

def playerChoice():
    usercolors = {
        "1": RED,
        "2": GREY,
        "3": GREEN,
        "4": YELLOW,
        "5": BLUE,
        "6": MAGENTA,
        "7": CYAN,
        "8": WHITE,
    }

    print("1 = " + str(RED))
    print("2 = " + str(GREY))
    print("3 = " + str(GREEN))
    print("4 = " + str(YELLOW))
    print("5 = " + str(BLUE))
    print("6 = " + str(MAGENTA))
    print("7 = " + str(CYAN))
    print("8 = " + str(WHITE))

    usrValue = int(input())
    usrValue = str(usrValue)

    numToColor = []

    for i in usrValue:
        numToColor.append(usercolors[i])

    print(" ".join(numToColor))



# print(' '.join(CPU))
