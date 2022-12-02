from filtering import filter
import numpy as np
import matplotlib.pyplot as plt


def main():
    world = input("Enter the world file: ")
    path = input("Enter path file: ")

    coords = []
    grid = {}

    try:
        with open(world, 'r') as f:
            coords = f.readlines()
    except:
        print("invalid input")
        return
    
    for line in coords:
        string = line.split()
        if string[2] 