import methods.decimal as decimal
import methods.vector as vec
from math import sqrt
from random import random

step = 4
gamma = 2
M = 3

def calculate(task):

    func = task.func
    xk = task.startpoint
    e = task.epsilon
    e1d = task.epsilon1d

    steep = step
    sigma = 1/gamma

    z = func.get(*xk)
    zn = z

    #print(steep)
    while True:
        #Step 2
        failsafe = 0

        while True:
            #Step 3
            rVec = vec.normalize((random()*2-1.,random()*2-1.))

            #Step 4
            p = vec.add(xk,vec.mulC(rVec, steep))
            zn = func.get(*p)
            #print(rVec,step,p)

            #Step 5
            if zn < z:
                xk = p
                z = zn
                continue

            #Step 6
            failsafe += 1
            if failsafe == M:
                #print('failsafe')
                break

        #Step 7
        if steep < e:
            return (*xk , zn)
        else:
            steep *= sigma
            failsafe = 0

