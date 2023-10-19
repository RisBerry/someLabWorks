from methods.base import frange
from math import *

def calculate(function, start, stop, epsilon):
    #Consts
    subdivision = 4
    ######
    minX = start
    maxX = stop

    step = (maxX-minX)/subdivision

    x0 = minX
    x1 = x0
    xm = minX
    Fx0 = function(x0)

    while True:
        x1 += step
        Fx1 = function(x1)
        #print(f'Debug| step:{step:.5f}| x1:{x1:.5f} | Fx1:{Fx1} | Fx0:{Fx0}')
        if (Fx1 > Fx0) or not (x1 > minX) or not (x1 < maxX):
            if abs(step) < epsilon:
                break
            x1 = min(max(x1,minX),maxX)
            step = -step/subdivision

        xm = x1
        Fx0 = Fx1
    return xm
