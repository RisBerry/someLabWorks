from methods.base import frange
from math import *

#From Lab1
#def calculate(task):
#    #Consts
#    subdivision = 4
#    ######
#    minX = task.xRange[0]
#    maxX = task.xRange[1]
#    epsilon = task.epsilon
#    function = task.function
#
#    step = (maxX-minX)/subdivision
#
#    x0 = minX
#    x1 = x0
#    xm = minX
#    Fx0 = function(x0)
#
#    itter = 0
#
#    while True:
#        itter+=1
#
#        x1 += step
#        Fx1 = function(x1)
#        #print(f'Debug| step:{step:.5f}| x1:{x1:.5f} | Fx1:{Fx1} | Fx0:{Fx0}')
#        if (Fx1 > Fx0) or not (x1 > minX) or not (x1 < maxX):
#            if abs(step) < epsilon:
#                break
#            step = -step/subdivision
#
#        xm = x1
#        Fx0 = Fx1
#
#    return (xm,Fx0,itter) 
