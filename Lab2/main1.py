from methods import base
from methods import slope,gradient
from methods.base import timeIt
from math import *

#import gc
#gc.disable()

#Default configuration
a = 1 #Doesn't matter (Change in brute A)
slope.vanilla = False
gradient.restart = 3

def bruteA(task):
    global a
    for i in (1,250,1000):
        a = i
        print(f'\nVariable A: {a}')
        timeIt(slope,task)
        timeIt(gradient,task)

def massExec(task):
    print(f'\nEpsilon: {task.epsilon}')
    bruteA(task)

derivX = base.function(
        lambda x,y : 2*x, #Func
        lambda x,y : 2  , #Deriv1
        lambda x,y : 0    #Deriv2
        )
derivY = base.function(
        lambda x,y : a*2*y, #Func
        lambda x,y : 0    , #Deriv1
        lambda x,y : a*2    #Deriv2
        )
func   = base.function(
        lambda x,y : x**2 + a * y**2,
        derivX,
        derivY
        )

task = base.task(func, .001, startpoint = (1., 1.))
massExec(task)
#base.plotTask(taskA1, 10)

task.epsilon = .00001
massExec(task)
