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

class Game:
    def __init__(self):
        self.ALLCOLORS = []
        self.count = 0
        self.CPU = []
        self.usercolors = {}
        self.usrValue = 0
        self.numTocolor = []


game = Game()

FullBlock = "\u2588"  # Create a fullblock
RED = colored(FullBlock, "red")
GREY = colored(FullBlock, "grey")
GREEN = colored(FullBlock, "green")
YELLOW = colored(FullBlock, "yellow")
BLUE = colored(FullBlock, "blue")
MAGENTA = colored(FullBlock, "magenta")
CYAN = colored(FullBlock, "cyan")
WHITE = colored(FullBlock, "white")

def startCPU():
    while copmputerChoice.count != 4:
        computerChoice.count += 1
        colors.ALLCOLORS= [RED, GREY, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
        random.shuffle(computerChoice.ALLCOLORS)
        computerChoice.CPU.append(colors.ALLCOLORS[0])




def playerChoice():
    game.usercolors = {
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

    game.usrValue = int(input())
    game.usrValue = str(game.usrValue)


    for i in game.usrValue:
        game.numToColor.append(game.usercolors[i])

    print(" ".join(game.numToColor))

playerChoice()

# print(' '.join(CPU))
