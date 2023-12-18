import methods.vector as v
import random
from math import exp

T = 100
Tstop = 0.0001
L = 2
a = 0.95

def setT(x):
    global T
    T = x

def setTstop(x):
    global Tstop
    Tstop = x

def setL(x):
    global L
    L = x

def seta(x):
    global a
    a = x

def calculate(task):
    task.reset()

    func = task.func
    size = func.dimensionSize

    startPoint = task.basepoint

    bestPoint = func.get(*startPoint) 
    cords = startPoint

    t = T

    random.seed(4321)

    while True:
        task.addTraceConverted(*cords)

        if t < Tstop:
            return (*func.indexToCords(*cords),bestPoint)

        task.itter += 1

        while True:
            #Generate random vector
            vec = v.mulC(v.normalize((random.random()*2-1,random.random()*2-1)),(1+random.random()*L))
            newCords = v.add(cords, vec)
            newCords = (min(max(newCords[0],0),func.dimensionSize-1),min(max(newCords[1],0),func.dimensionSize-1))
            if newCords == cords:
                continue
            break

        point = func.get(*newCords)
        delta = point - bestPoint

        if delta < 0:
            bestPoint = point
            cords = newCords
        else:
            n = random.random()
            prob = exp(-delta/t)
            if n < prob:
                bestPoint = point
                cords = newCords
        t *= a
