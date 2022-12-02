from filtering import filter
import numpy as np
import matplotlib.pyplot as plt


def main():
    world = input("Enter the world file: ")
    path = input("Enter path file: ")

    coords = []
    bot = []
    grid = {}

    truePath = []
    moves = []
    evidence = []

    try:
        with open(world, 'r') as f:
            coords = f.readlines()
    except:
        print("invalid input")
        return
    
    for line in coords:
        string = line.split()
        if string[2] != "B":
            grid[(string[0], string[1])] = string[2]
    
    f.close()

    try:
        with open("paths" + "/" + path, 'r') as f:
            bot = f.readlines()
    except:
        print("invalid input")
        return

    for step in range(1, 101):
        cell = path[step].split()
        truePath.append((cell[0], cell[1]))

    for step in range(101, 201):

    