import random

dict = {}

def transition(move, coor):
    choice = random.choices(['move','stay'], [9, 1], k = 1)[0]
    if choice == 'stay':
        return coor
    else:
        match move:
            case 'D':
                return (coor[0] + 1, coor[1])
                
            case 'R':
                return (coor[0], coor[1] + 1)
            
            case 'L':
                return (coor[0], coor[1] - 1)

            case 'U':
                return (coor[0] - 1, coor[1])

def observation(truth):
    types = ['N', 'H', 'T']
    choices = [truth]
    for letter in types:
        if letter not in choices:
            choices.append(letter)
        
    return random.choices(choices, [90, 5, 5], k=1)[0]


def main():
    
    for x in range(10):
        testFile = input("Please enter the name of the test file to generate on: ")
        for y in range(10):
            dict.clear()
            coords = []
            try:
                with open(testFile, 'r') as f:
                    coords = f.readlines()
            except:
                print("invalid input")
                return
            

            for line in coords:
                string = line.split()
                if string[2] != 'B':
                    coor = (int(string[0]), int(string[1]))
                    dict[coor] = string[2]

            f.close()


            startX = random.randint(1, 101) #returns a num bet 1 and m inclusive
            startY = random.randint(1, 51) #returns a num bet 1 and n inclusive
            while((startX, startY) not in dict): #Make sure that the init is not blocked
                startX = random.randint(1, 101) #returns a num bet 1 and m inclusive
                startY = random.randint(1, 51) #returns a num bet 1 and n inclusive

            path = []
            moves = []
            evidence = []
            coor = (startX, startY)

            for i in range(100):
                move = random.choice(['U', 'D', 'L', 'R'])
                moves.append(move)
                newCoor = transition(move, coor)
                if newCoor in dict:
                    coor = newCoor
                path.append(coor)
                evidence.append(observation(dict.get(coor)))


            strNum = "path" + str(x) + "_" + str(y)
            fileName = strNum + ".txt"
            with open(fileName, 'w') as f:
                fileString = str(startX) +" " + str(startY) + "\n"
                for cell in path:
                    fileString = fileString + str(cell[0]) + " " + str(cell[1]) + "\n"

                for letter in moves:
                    fileString = fileString + letter + "\n"

                for ob in evidence:
                    fileString = fileString + ob + "\n"

                f.write(fileString)



main()
