
import random
dict = {}
def main():
    for x in range(10):
        dict.clear()
        strNum = "world" + str(x)
        fileName= strNum + ".txt"
        with open(fileName, 'w') as f: #creates a new file with name test1...50
            row = 50
            col = 100
            fileString = ""
            blockedPicker(col, row)
            # startX = random.randint(1, col + 1) #returns a num bet 1 and m inclusive
            # startY = random.randint(1, row + 1) #returns a num bet 1 and n inclusive
            # while((startX, startY) not in dict): #Make sure that the init is not blocked
            #      startX = random.randint(1, col + 1) #returns a num bet 1 and m inclusive
            #      startY = random.randint(1, row + 1) #returns a num bet 1 and n inclusive
            # fileString = fileString + str(startX) +" " + str(startY) + "\n"
            hardPicker(col, row)
            highwayPicker(col, row)
            #grid size - n columns and m rows
            
            gridSize = (col+ 1,row + 1)
            #fileString = fileString + str(col) + " " + str(row) + "\n"
            
            # load file with index information
            for i in range(gridSize[0]):
                if i == 0 :
                    continue
                for j in range(gridSize[1]):
                    if j == 0:
                        continue
                    if (i, j) in dict:
                        val = dict.get((i, j))
                        if (val == "b"):
                            fileString = fileString + str(i) +" " + str(j) + " " + "B" + "\n"
                        elif (val == "h"):
                            fileString = fileString + str(i) +" " + str(j) + " " + "H" + "\n"
                        else:
                            fileString = fileString + str(i) +" " + str(j) + " " + "T" + "\n"
                    else:
                        fileString = fileString + str(i) +" " + str(j) + " " + "N"   + "\n"
            f.write(fileString)
        print ("done")

               

# Picks 10% of MxN unique indexes to be blocked 
def blockedPicker(col, row):
    tenPercent = int(round(col*row*.1))
    count = 0
    for i in range(tenPercent):
        xy = (random.randint(1,col + 1), random.randint(1,row + 1))
        while xy in dict :
            xy = (random.randint(1,col + 1), random.randint(1,row + 1))
        dict[xy] = "b"
        count = count +1
    #return dict
    print("blocked" + str(count))

# Picks 20% of MxN unique indexes to be hard 
def hardPicker(col, row):
    twntyPercent = int(round(col*row*.2))
    count = 0
    for i in range(twntyPercent):
        xy = (random.randint(1,col + 1), random.randint(1,row + 1))
        while xy in dict : #goes until it finds one not in the dict already
            xy = (random.randint(1,col + 1), random.randint(1,row + 1))
        dict[xy] = "h"
        count = count + 1
    #return dict
    print("hard" + str(count))

# Picks 20% of MxN unique indexes to be highway 
def highwayPicker(col, row):
    twntyPercent = int(round(col*row*.2))
    count = 0
    for i in range(twntyPercent):
        xy = (random.randint(1,col + 1), random.randint(1,row + 1))
        while xy in dict :
            xy = (random.randint(1,col + 1), random.randint(1,row + 1))
        dict[xy] = "t"
        count = count + 1
    #return dict
    print("highway" + str(count))
main()
