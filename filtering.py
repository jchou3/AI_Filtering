


#Parameters:
#   grid: a dictionary mapping a tuple of coordinates to their terrain, i.e. {(1, 1):H}. Does not include blocked cells.
#   moves: list of moves in order as uppercase characters, i.e. ['U', 'L', 'R', 'D']
#   evidence: list of evidence sensed as uppercase characters, i.e. ['N', 'H', 'T']
#   t: which iteration the filtering is currently operating on

#To start filtering process, call filtering(len(moves) - 1, grid, moves, evidence), returns final probability distribution
#To find the probability distribution after move t, you can also just call filtering(t - 1, .....)


#normalizes over a probability distribution
def normalize(distribution):
    sum = 0
    for key, value in distribution.items():
        sum += value

    for key, value in distribution.items():
        distribution[key] = distribution.get(key)/sum

    return distribution



#Recursively filters
#   prev: probability distribution of the previous iteration
def bigFilter(t, grid, moves, evidence):

    if t > 0:
        prev = bigFilter(t - 1, grid, moves, evidence)
    else:
        initial_distribution = dict()
        for key, value in grid.items():
            initial_distribution[key] = 1
        prev = normalize(initial_distribution)

    new_belief = {}

    for key, value in grid.items():
        om = .9 if evidence[t] == value else .05
        pm = PM(prev, moves[t], key, grid)
        new_belief[key] = om * pm
    
    new_belief = normalize(new_belief)
    return new_belief


#Recursively filters
#   prev: probability distribution of the previous iteration
def filter(prev, grid, move, evidence):


    new_belief = {}

    for key, value in grid.items():
        om = .9 if evidence == value else .05
        pm = PM(prev, move, key, grid)
        new_belief[key] = om * pm
    
    new_belief = normalize(new_belief)
    return new_belief


#Returns prediction model value
def PM(prev, move, coor, grid):
    next = {'U':'D', 'D':'U', 'L':'R', 'R':'L'}

    pm = .1 * prev.get(coor)
    old = transition(move, coor)
    ahead = transition(next.get(move), coor)

    if old in grid:
        pm += .9 * prev.get(old)
    
    if ahead not in grid:
        pm += .9 * prev.get(coor)
    
    return pm

#returns coordinate of previous spot given a move, returns old move if 
def transition(move, coor):
    match move:
        case 'U':
            return (coor[0] + 1, coor[1])
            
        case 'L':
            return (coor[0], coor[1] + 1)
        
        case 'R':
            return (coor[0], coor[1] - 1)

        case 'D':
            return (coor[0] - 1, coor[1])
            


# grid = {
#         (1, 1): 'H',
#         (1, 2): 'H',
#         (1, 3): 'T',
#         (2, 1): 'N',
#         (2, 2): 'N',
#         (2, 3): 'N',
#         (3, 1): 'N',
#         (3, 3): 'H'
#     }

# moves = ['R', 'R', 'D', 'D']
# evidence = ['N', 'N', 'H', 'H']

# filtering(len(moves) - 1, grid, moves, evidence)

