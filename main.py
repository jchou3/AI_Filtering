from filtering import filter
from filtering import normalize
import numpy as np
import matplotlib.pyplot as plt


def main():
    world = input("Enter the world file: ")
    path = input("Enter path file: ")
    speed = input("How fast would you like to run the visualization (in seconds per step)? ")

    s = float(speed)

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
            grid[int(string[0]), int(string[1])] = string[2]
    
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
        move = bot[step].split()[0]
        moves.append(move)
    
    for step in range(201, 301):
        observe = bot[step].split()[0]
        evidence.append(observe)

    f.close()
    
    #Note: 100 cols x 50 rows, but input is in row, col order
    prediction = initialize(grid)
    initial = np.zeros((51, 101), dtype = float)
    data = tonumpy(prediction, initial)
    fig = plt.imshow(data, cmap = 'autumn', interpolation = 'none', aspect = 'equal')
    plt.title("Prediction at t = {}".format(0))
    plt.grid(color = "b", linestyle = "-", visible = True)
    plt.draw()
    plt.pause(s)

    for i in range(100):
        move = moves[i]
        observation = evidence[i]

        prediction = filter(prediction, grid, move, observation) #gets dictionary of next step
        data = tonumpy(prediction, initial) #puts info into numpy

        fig.set_data(data)

        spot = mostLikely(prediction)
        if len(spot) <= 5:
            print(spot)
            
        plt.title("Prediction at t = {}".format(i + 1))
        plt.draw() #draws new heatmap
        plt.pause(s)

    plt.show()




def initialize(grid):
    initial_distribution = dict()
    for key, value in grid.items():
        initial_distribution[key] = 1
    return normalize(initial_distribution)


def tonumpy(dict, array):
    for key, val in dict.items():
        array[key[0]][key[1]] = val

    return array


def mostLikely(dict):
    max_keys = [key for key, value in dict.items() if value == max(dict.values())]
    return max_keys

main()