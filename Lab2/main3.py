from methods import base
from methods import slope,gradient,newton,simplex,cycle,hj,rnd
from methods.base import timeIt
from math import *

#import gc
#gc.disable()

#Default configuration
slope.vanilla = False
slope.correction = 4

gradient.restart = 3
gradient.correction = 2

simplex.vanilla = True
simplex.useGrad = False
simplex.l = 1
simplex.sigma = 0.95
simplex.alwaysDump = False
simplex.allowTriangleFlip = True

cycle.vanilla = True
cycle.step = 3

hj.vanilla = False
hj.alternativeVectors = True
hj.step = 1
hj.gamma = 2

rnd.M = 200


def massExec(task):
    print(f'\nEpsilon: {task.epsilon}')
    timeIt(slope,task)
    timeIt(gradient,task)
    timeIt(newton,task)
    timeIt(simplex,task)
    timeIt(cycle,task)
    timeIt(hj,task)
    timeIt(rnd,task)

derivX = base.function(
        lambda x,y : 2*(200*x*(x**2-y)+x-1), #Func
        lambda x,y : 1200*x**2-400*y, #Deriv1
        lambda x,y : -400*x #Deriv2
        )
derivY = base.function(
        lambda x,y : -200*(x**2-y), #Func
        lambda x,y : -400*x, #Deriv1
        lambda x,y : 200     #Deriv2
        )
func   = base.function(
        lambda x,y : 100*(x**2-y)**2+(x-1)**2,
        derivX,
        derivY
        )

task = base.task(func, .001, startpoint = (-1., 1.))
#task.epsilon1d = .00000001
task.epsilon1d = .000001

task.epsilon = .1
#base.plotTask(task, 3)

task.epsilon = .001
massExec(task)

task.epsilon = .00001
task.epsilon1d = .00000001
#task.epsilon1d = .00001
massExec(task)
