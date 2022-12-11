from filtering import filter
from filtering import normalize
import numpy as np
import matplotlib.pyplot as plt
import math
import random


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

    cell = bot[0].split()
    start = ((int(cell[0]), int(cell[1])))

    for step in range(1, 101):
        cell = bot[step].split()
        truePath.append((int(cell[0]), int(cell[1])))

    for step in range(101, 201):
        move = bot[step].split()[0]
        moves.append(move)
    
    for step in range(201, 301):
        observe = bot[step].split()[0]
        evidence.append(observe)

    f.close()
    
    #info needed for plotting

    #Probability value at the ground truth at every step
    truePred = []

    #Distance between most likely and ground truth at each step after t = 5
    distance = []

    #Note: 100 cols x 50 rows, but input is in row, col order
    prediction = initialize(grid)
    truePred.append(prediction[start])
    initial = np.zeros((51, 101), dtype = float)
    data = tonumpy(prediction, initial)

    figure, axis = plt.subplots(3, 1)

    fig = axis[0].imshow(data, cmap = 'autumn', interpolation = 'none', aspect = 'equal')
    axis[0].title.set_text("Prediction at t = {}".format(0))
    axis[0].grid(color = "b", linestyle = "-", visible = True)
    plt.draw()
    plt.pause(s)

    for i in range(100):
        move = moves[i]
        observation = evidence[i]

        prediction = filter(prediction, grid, move, observation) #gets dictionary of next step
        data = tonumpy(prediction, initial) #puts info into numpy

        truePred.append(prediction[truePath[i]])

        fig.set_data(data)

        if i > 4:
            spot = mostLikely(prediction)
            distance.append(getDistance(truePath[i], spot))


            
        axis[0].set_title("Prediction at t = {}".format(i + 1))
        plt.draw() #draws new heatmap
        plt.pause(s)

    
    distanceX = [i for i in range(5, 100)]
    truePredX = [i for i in range(len(truePred))]

    print(spot)
    print(truePred[len(truePred) - 1])

    axis[1].plot(distanceX, distance)
    axis[1].set_title("Distance between Ground Truth and Most Likely Prediction")

    axis[2].plot(truePredX, truePred)
    axis[2].set_title("Probability at Ground Truth over steps")


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
    return random.choice(max_keys)


#Coordinates given as tuples
def getDistance(a, b):
    ax = a[0]
    ay = a[1]
    bx = b[0]
    by = b[1]

    x = abs(ax - bx)
    y = abs(ay - by)

    dist = math.sqrt((x^2) + (y^2))
    return dist

main()