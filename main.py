from filtering import filter
from filtering import normalize
import numpy as np
import matplotlib.pyplot as plt
import math
import random


def main(world, path, s):


    # s = float(speed)

    coords = []
    bot = []
    grid = {}

    truePath = []
    moves = []
    evidence = []



    #reads world file, builds grid (without blocked cells)
    try:
        with open("worlds/" + world, 'r') as f:
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
        with open("paths/" + path, 'r') as f:
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

    # Probability value at the ground truth at every step
    # truePred = []

    #Distance between most likely and ground truth at each step after t = 5
    # distance = []

    #Note: 100 cols x 50 rows, but input is in row, col order
    prediction = initialize(grid)
    # truePred.append(prediction[start])
    initial = np.zeros((51, 101), dtype = float)
    data = tonumpy(prediction, initial)


    #Code for plotting

    fig = plt.imshow(data, cmap = 'autumn', interpolation = 'none', aspect = 'equal')
    plt.title("Prediction at t = {}".format(0))
    plt.grid(color = "b", linestyle = "-", visible = True)
    dot = plt.plot(start[1], start[0], "bo")
    plt.draw()
    if s > 0:
        plt.pause(s)

    for i in range(100):
        move = moves[i]
        observation = evidence[i]

        prediction = filter(prediction, grid, move, observation) #gets dictionary of next step
        data = tonumpy(prediction, initial) #puts info into numpy

        # truePred.append(prediction[truePath[i]])

        fig.set_data(data)


        # Gets most likely
        # if i > 4:
        #     spot = mostLikely(prediction)
            # distance.append(getDistance(truePath[i], spot))

        
        #Code for plotting true path and stopping at specific iterations

        # if i == 10:
        #     curTruth = [start] + truePath[0:i]
        #     # x = [x[0] for x in curTruth]
        #     # y = [x[1] for x in curTruth]
        #     print(curTruth)
        #     for k in range(len(curTruth) - 1):
        #         plt.plot([curTruth[k][1], curTruth[k + 1][1]], [curTruth[k][0], curTruth[k + 1][0]], "b-")
        #     dot = plt.plot(curTruth[i][1], curTruth[i][0], "bo")
        #     plt.draw()
        #     plt.pause(15)
        #     linePath = dot.pop()
        #     linePath.remove()


        # if i == 50:
        #     curTruth = [start] + truePath[0:i]
        #     # x = [x[0] for x in curTruth]
        #     # y = [x[1] for x in curTruth]
        #     for k in range(10, len(curTruth) - 1):
        #         plt.plot([curTruth[k][1], curTruth[k + 1][1]], [curTruth[k][0], curTruth[k + 1][0]], "b-")
        #     dot2 = plt.plot(curTruth[i][1], curTruth[i][0], "bo")
        #     plt.draw()
        #     plt.pause(15)
        #     linePath = dot2.pop()
        #     linePath.remove()


        drop = dot.pop()
        drop.remove()

        dot = plt.plot(truePath[i][1], truePath[i][0], "bo")

        plt.title("Prediction at t = {}".format(i + 1))
        plt.draw() #draws new heatmap

        

        if s > 0:
            plt.pause(s)


    # Code for plotting distance and probability plots
    # distanceX = [i for i in range(5, 100)]
    # truePredX = [i for i in range(len(truePred))]

    # axis[1].plot(distanceX, distance)
    # axis[1].set_title("Distance between Ground Truth and Most Likely Prediction")

    # axis[2].plot(truePredX, truePred)
    # axis[2].set_title("Probability at Ground Truth over steps")

    # Code for plotting true path
    # curTruth = [start] + truePath[:100]
    # for k in range(50, len(curTruth) - 1):
    #     plt.plot([curTruth[k][1], curTruth[k + 1][1]], [curTruth[k][0], curTruth[k + 1][0]], "b-")
    # plt.plot(curTruth[100][1], curTruth[100][0], "bo")
    # plt.draw()
    # plt.pause(10)



    plt.show()


    # return distance, truePred


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


world = input("Enter the world file: ")
path = input("Enter path file: ")
speed = input("How fast would you like to run the visualization (in seconds per step)? ")

main(world, path, float(speed))

# totalDistance = [0] * 95
# totalProb = [0] * 101

# for i in range(10):
#     world = "world" + str(i) + ".txt"
#     print("On world " + str(i))
#     for k in range(10):
#         path = "path" + str(i) + "_" + str(k) + ".txt"
#         distances, probabilities = main(world, path)

#         for n in range(len(distances)):
#             totalDistance[n] += distances[n]
#         for m in range(len(probabilities)):
#             totalProb[m] += probabilities[m]


# distanceX = [i for i in range(5, 100)]
# truePredX = [i for i in range(len(totalProb))]

# iterations = 100

# d = [x/iterations for x in totalDistance]
# p = [x/iterations for x in totalProb]

# figure, axis = plt.subplots(2, 1)
# axis[0].plot(distanceX, d)
# axis[0].set_title("Distance between Ground Truth and Most Likely Prediction")

# axis[1].plot(truePredX, p)
# axis[1].set_title("Probability at Ground Truth Cell")

# plt.show()