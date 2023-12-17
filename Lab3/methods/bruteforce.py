from math import sqrt,sin,cos,pi
from random import random

def calculate(task):
    task.reset()

    func = task.func
    size = func.dimensionSize

    startPoint = task.basepoint

    bestPoint = func.get(*startPoint) 
    cords = startPoint

    for i in range(size):
        for j in range(size):
            task.itter += 1

            task.addTraceConverted(i,j)

            point = func.get(i,j)

            if point < bestPoint:
                bestPoint = point
                cords = (i,j)

    return (*func.indexToCords(*cords),bestPoint)
