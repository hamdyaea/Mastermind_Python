#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

from termcolor import colored
import random

def coloredBlocks():
    global RED, GREY, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

    FullBlock = u"\u2588" # Create a fullblock

    RED = colored(FullBlock, "red")
    GREY = colored(FullBlock, "grey")
    GREEN = colored(FullBlock, "green")
    YELLOW = colored(FullBlock, "yellow")
    BLUE = colored(FullBlock, "blue")
    MAGENTA = colored(FullBlock, "magenta")
    CYAN = colored(FullBlock, "cyan")
    WHITE = colored(FullBlock, "white")
    



def computerChoice():
    count = 0
    CPU = []
    while count != 4:
        count += 1
        ALL = [RED,GREY,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE]
        random.shuffle(ALL)
        CPU.append(ALL[0])

    for i in CPU:
        print(i)
coloredBlocks()
computerChoice()
