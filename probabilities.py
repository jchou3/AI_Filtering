import random
import matplotlib.pyplot as plt
import numpy as np

probabilities = {
    'a' : 0.0,
    'b' : 0.9,
    'c' : {('a', 'b'): 0.2, ('a', '-b'): 0.6, ('-a', 'b'):0.5, ('-a','-b'): 0.0},
    'd' : {('b', 'c'): 0.75, ('b', '-c'): 0.1, ('-b', 'c'):0.5, ('-b','-c'):0.2}
}

def createSample():

    a = {'a': '-a'}
    b = {'b' : random.choices(['b', '-b'], [0.9, 0.1], k = 1)[0]}
    ab = ('-a', b.get('b'))
    c = {'c' : random.choices(['c', '-c'], [probabilities.get('c').get(ab), 1 - probabilities.get('c').get(ab)], k = 1)[0]}
    bc = (b.get('b'), c.get('c'))
    d = {'d' : random.choices(['d', '-d'], [probabilities.get('d').get(bc), 1 - probabilities.get('d').get(bc)], k = 1)[0]}

    values = {}
    values.update(a)
    values.update(b)
    values.update(c)
    values.update(d)

    return values

def createWeight(given):

    w = 1
    a = {'a': '-a'}
    if '-b' in given:
        b = {'b' : '-b'}
        w = w * 0.1
    else:
        b = {'b' : random.choices(['b', '-b'], [0.9, 0.1], k = 1)[0]}

    ab = ('-a', b.get('b'))

    if 'c' in given:
        c = {'c' : 'c'}
        w = w * probabilities.get('c').get(ab)
    else:
        c = {'c' : random.choices(['c', '-c'], [probabilities.get('c').get(ab), 1 - probabilities.get('c').get(ab)], k = 1)[0]}

    bc = (b.get('b'), c.get('c'))

    if 'd' in given:
        d = {'d' : 'd'}
        w = w * probabilities.get('d').get(bc)
    else:
        d = {'d' : random.choices(['d', '-d'], [probabilities.get('d').get(bc), 1 - probabilities.get('d').get(bc)], k = 1)[0]}

    values = {}
    values.update(a)
    values.update(b)
    values.update(c)
    values.update(d)
    values['weight'] = w

    return values




def reject(given, samples):
    cur = []
    for sample in samples:
        match = True
        for key, val in given.items():
            if sample[key] != val:
                match = False
        if match:
            cur.append(sample)
    return cur


def normalize(distribution):
    sum = 0
    for number in distribution:
        sum += number

    newDistribution = []
    for number in distribution:
        newDistribution.append(number/sum)

    return newDistribution

def main():

    sampNum = []
    rejProb = []
    likeProb = []

    for i in range(20, 2000, 20):
        sampNum.append(i)
        rejSamples = []
        for n in range(i):
            rejSamples.append(createSample())

        first = {'b':'-b'}
        firstSamples = reject(first, rejSamples)

        # third = {'a':'-a', 'b':'b'}
        # thirdSamples = reject(third, rejSamples)


        firstDistribution = [0, 0]
        for sample in firstSamples:
            if sample['d'] == 'd':
                firstDistribution[0] += 1
            else:
                firstDistribution[1] += 1
        firstDistribution = normalize(firstDistribution)

        # s = [0, 0]
        # for sample in firstSamples:
        #     if sample['b'] == 'b':
        #         s[0] += 1
        #     else:
        #         s[1] += 1
        # s = normalize(s)

        # t = [0, 0]
        # for sample in thirdSamples:
        #     if sample['d'] == 'd':
        #         t[0] += 1
        #     else:
        #         t[1] += 1
        # t = normalize(t)

        # print("Rejection Sampling: \n")
        # print("P(d|c) = " + str(firstDistribution[0]) + "\n")
        rejProb.append(firstDistribution[0])
        # print("P(b|c) = " + str(s[0]) + "\n")
        # print("P(d|-a, b) = " + str(t[0]) + "\n")



        likeSamplesf = []
        for n in range(i):
            likeSamplesf.append(createWeight(['-b']))

        # ts = []
        # for n in range(i):
        #     ts.append(createWeight(['b']))

        fl = [0, 0]
        # sl = [0, 0]
        # tl = [0, 0]

        for sample in likeSamplesf:
            if sample['d'] == 'd':
                fl[0] += sample['weight']
            else:
                fl[1] += sample['weight']
        fl = normalize(fl)

        # for sample in likeSamplesf:
        #     if sample['b'] == 'b':
        #         sl[0] += sample['weight']
        #     else:
        #         sl[1] += sample['weight']
        # sl = normalize(sl)

        # for sample in ts:
        #     if sample['d'] == 'd':
        #         tl[0] += sample['weight']
        #     else:
        #         tl[1] += sample['weight']
        # tl = normalize(tl)

        # print("Likelihood Weighing: \n")
        # print("P(d|c) = " + str(fl[0]) + "\n")
        # print("P(b|c) = " + str(sl[0]) + "\n")
        # print("P(d|-a, b) = " + str(tl[0]) + "\n")
        likeProb.append(fl[0])

    sampNum = np.array(sampNum)
    rejProb = np.array(rejProb)
    likeProb = np.array(likeProb)

    plt.plot(sampNum, rejProb, label = "Rejection Sampling")
    plt.plot(sampNum, likeProb, label = "Likelihood Weighing")

    plt.legend()
    plt.show()

    

main()