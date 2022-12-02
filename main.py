from filtering import filter
from filtering import normalize
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

    #reads world file, builds grid (without blocked cells)
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


    #reads path file, creates true path, moves, and evidence
    try:
        with open("paths" + "/" + path, 'r') as f:
            bot = f.readlines()
    except:
        print("invalid input")
        return

    for step in range(1, 101):
        cell = bot[step].split()
        truePath.append((cell[0], cell[1]))

    for step in range(101, 201):
        move = bot[step]
        moves.append(move)
    
    for step in range(201, 301):
        observe = bot[step]
        evidence.append(observe)

    f.close()
    
    #Note: 100 cols x 50 rows, but input is in row, col order
    prediction = initialize(grid)
    initial = np.zeros((50, 100))

    data = tonumpy(prediction, initial)
    fig = plt.imshow(data, cmap = 'autumn', interpolation = 'none', aspect = 'equal')


    for i in range(100):
        move = moves[i]
        observation = evidence[i]






def initialize(grid):
    initial_distribution = dict()
    for key, value in grid.items():
        initial_distribution[key] = 1
    return normalize(initial_distribution)


def tonumpy(dict, array):
    pass
