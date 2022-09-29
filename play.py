#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

from termcolor import colored
import random
import os

os.system("cls||clear")  # Clear the terminal


def coloredBlocks():
    global RED, GREY, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

    FullBlock = "\u2588"  # Create a fullblock

    RED = colored(FullBlock, "red")
    GREY = colored(FullBlock, "grey")
    GREEN = colored(FullBlock, "green")
    YELLOW = colored(FullBlock, "yellow")
    BLUE = colored(FullBlock, "blue")
    MAGENTA = colored(FullBlock, "magenta")
    CYAN = colored(FullBlock, "cyan")
    WHITE = colored(FullBlock, "white")


def computerChoice():
    global CPU
    count = 0
    CPU = []
    while count != 4:
        count += 1
        ALL = [RED, GREY, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
        random.shuffle(ALL)
        CPU.append(ALL[0])


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


coloredBlocks()
computerChoice()
playerChoice()

# print(' '.join(CPU))
