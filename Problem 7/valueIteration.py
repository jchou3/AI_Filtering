import time
def valueIteration (reward, transition, states, actionsPerState, possibleMoves):
    ###################
    # Value Iteration Pseudocode


    # input (All states "S", all possible Actions "A", 
    # transition model (probability of getting from one state to next)) "S",
    # and reward table "R")
    # k = 0
    # For all states in S, InitialiZe Vk(s) with an arbitrary value, let's set it to 0 at first.
    # for all states s in S
        # 

    ###################
    maxIterations = 100000
    values = {}
    policies = {}
    for s in states: #init value table all to 0
        values[s] = 0
        policies[s] = 0 #impossible action, actions are 1-4
    # loop through the following until |current value at any state - previous value at any state| is very small
    i = 0
    for i in range(maxIterations): # PLACEHOLDER
        newVals = {}
        difference = 0
        for s in states:
            newVals[s] = 0
        for s in states:
            # find max action in action 
            maximum = 0
            for a in actionsPerState[s]:
                val = reward[s]
                for p in possibleMoves[s]: 
                    tran = tuple([s, a, p])
                    if tran in transition:
                        val += 0.9 * transition[tuple([s, a, p])] * values[p]
                        val
                maximum = max(maximum, val)
                if values[s] < val:
                    policies[s] = a
            newVals[s] = maximum
            difference = max(difference, abs(values[s] - newVals[s]))
        values = newVals
        if i % 10 == 0:
            print("Iteration : " + str(i))
            print("Values : (State to Value) " + str(values))
            print("Policies : (State to Action)" + str(policies))
            print()
        if difference < 0.001:
            print("Iteration : " + str(i))
            print("Values : (State to Value) " + str(values))
            print("Policies : (State to Action)" + str(policies))
            print()
            break
    return policies




def main():
    # need to define state space
    # available actions
    # reward table
    reward = {
        1 : 0, 
        2 : 0, 
        3 : 1, 
        4 : 0
    }
    # transition model
    # just make a hashtable with state, action, next state as key, probability as value.
    # in the format (state, action, other state) represented by integers
    transition = {
        tuple([1, 1, 1]) : 0.2, 
        tuple([1, 1, 2]) : 0.8, 
        tuple([1, 2, 1]) : 0.2,
        tuple([1, 2, 4]) : 0.8,
        tuple([2, 2, 2]) : 0.2,
        tuple([2, 2, 3]) : 0.8,
        tuple([2, 3, 2]) : 0.2,
        tuple([2, 3, 1]) : 0.8,
        tuple([3, 4, 2]) : 1,
        tuple([3, 3, 4]) : 1,
        tuple([4, 1, 4]) : 0.1,
        tuple([4, 1, 3]) : 0.9,
        tuple([4, 4, 4]) : 0.2,
        tuple([4, 4, 1]) : 0.8
        }

    states = [1, 2, 3, 4]

    actionsPerState = {
        1 : [1, 2],
        2 : [2, 3],
        3 : [3, 4],
        4 : [1, 4]
    }

    possibleMoves = {
        1 : [1, 2, 4],
        2 : [2, 3, 1],
        3 : [4, 2],
        4 : [4, 3, 1]
    }

    startTime = time.time()
    optimalPolicies = valueIteration(reward, transition, states, actionsPerState, possibleMoves)
    print("Time to complete : " + str(time.time()-startTime))


main()
