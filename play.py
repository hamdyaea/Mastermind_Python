#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

from termcolor import colored
import random
import os
import logging

try:  # Try to clear the terminal if not possible pass.
    os.system("cls||clear")  # Clear the terminal
except Exception as e:
    logging.warning(e)
    pass


class Game:
    def __init__(self):
        self.ALLCOLORS = []
        self.count = 0
        self.CPU = []
        self.usercolors = {}
        self.usrValue = 0
        self.numToColor = []


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
    while game.count != 4:
        game.count += 1
        game.ALLCOLORS = [RED, GREY, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
        random.shuffle(game.ALLCOLORS)
        game.CPU.append(game.ALLCOLORS[0])
    print("Computer colors : ")
    print(" ".join(game.CPU))


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


def enterNum():
    game.numToColor = []
    game.usrValue = ""
    print("Enter 4 numbers : ")
    try:
        game.usrValue = int(input())
    except Exception as e:
        logging.error(e)
        enterNum()
    game.usrValue = str(game.usrValue)

    for i in game.usrValue:
        game.numToColor.append(game.usercolors[i])

    if len(game.numToColor) != 4:
        enterNum()
    if len(game.numToColor) == 4:
        print("Player colors : ")
        print(" ".join(game.numToColor))


playerChoice()
startCPU()
enterNum()
