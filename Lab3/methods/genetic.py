import methods.vector as v
import random
from math import exp

N = 50
maxItter = 50

#Population alive size
a = 0.5
#Population restore
b = 0.8

def setN(x):
    global N
    N = x

def setmaxItter(x):
    global maxItter
    maxItter = x

def seta(x):
    global a
    a = x

def setb(x):
    global b
    b = x

def genPoint(herd,func):
    point = None

    #HARDCODE
    dimSize = 40

    while True:
        point = (random.randrange(0,dimSize),random.randrange(0,dimSize))
        point = (*point, func.get(*point))
        if point in herd:
            continue
        break

    return point

def calculate(task):
    task.reset()

    func = task.func
    size = func.dimensionSize

    startPoint = task.basepoint

    random.seed(451+hash(tuple(startPoint))) #Randomize seed, base on start point

    herd = [(*startPoint,func.get(*startPoint))]

    for i in range(N - 1):
        herd.append(genPoint(herd,func))
    herd.sort(key = lambda x: x[2])

    while True:
        task.addTraceConverted(*herd[0][:2])

        if task.itter == maxItter:
            return (*func.indexToCords(*herd[0][:2]),herd[0][2])
        
        #Begin massacre
        herd = herd[:int(len(herd)*a)]

        #Crossover new (up to N*b)
        tmpHerd = herd.copy()

        failsafe = N
        while len(herd) < int(N*b):
            failsafe -= 1
            if failsafe == 0 or len(herd) <= 2:
                break

            crossPoint = None

            parent1,parent2 = random.sample(tmpHerd, 2)
            
            #crossPoint = (parent1[random.randrange(2)],parent2[random.randrange(2)])
            crossPoint = (parent1[0],parent2[1])
            crossPoint = (*crossPoint, func.get(*crossPoint))

            #Trying to create uniqe individuals
            if crossPoint in herd:
                continue

            herd.append(crossPoint)

        #Mutate (a.k.a refill with new individuals)
        while len(herd) < int(N):
            herd.append(genPoint(herd,func))

        #Sort herd
        herd.sort(key = lambda x: x[2])

        task.itter += 1
