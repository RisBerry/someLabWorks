from methods import base
from methods import slope,gradient,newton,simplex,cycle,hj,rnd
from methods.base import timeIt
from math import *

#import gc
#gc.disable()

#Default configuration
slope.vanilla = False
gradient.restart = 3

simplex.vanilla = True
simplex.useGrad = False
simplex.l = 3
simplex.sigma = 0.85
simplex.alwaysDump = False
simplex.allPoints = False
simplex.allowTriangleFlip = True

cycle.vanilla = True
cycle.step = 3

newton.jitter = False
newton.decimalSearch = True
newton.decimalLength = 2.

hj.vanilla = False
hj.alternativeVectors = True
hj.step = 1
hj.gamma =  2

rnd.M = 200


def massExec(task):
    print(f'\nEpsilon: {task.epsilon}')
    print(f'Basepoint: {task.startpoint}\n')
    timeIt(slope,task)
    timeIt(gradient,task)
    timeIt(newton,task)
    timeIt(simplex,task)
    timeIt(cycle,task)
    timeIt(hj,task)
    timeIt(rnd,task)

derivX = base.function(
        lambda x,y : 2*(2*x*(x*x+y-11)+x+y*y-7), #Func
        lambda x,y : 12*x*x+4*y-42, #Deriv1
        lambda x,y : 4*(x+y)  #Deriv2
        )
derivY = base.function(
        lambda x,y : 2*(x*x+2*y*(x+y*y-7)+y-11), #Func
        lambda x,y : 4*(x+y), #Deriv1
        lambda x,y : 4*x+12*y*y-26  #Deriv2
        )
func   = base.function(
        lambda x,y : (x*x+y-11)**2+(x+y*y-7)**2,
        derivX,
        derivY
        )

task = base.task(func, .001, startpoint = (0., 0.))
#task.epsilon1d = .00000001

#task.epsilon = .1
#base.plotTask(task, 5)

task.epsilon = .001
task.epsilon1d = .000001
massExec(task)

task.epsilon = .00001
task.epsilon1d = .00000001
massExec(task)


task.startpoint = (-5., 0.)
task.epsilon = .001
task.epsilon1d = .000001
massExec(task)

task.epsilon = .00001
task.epsilon1d = .00000001
massExec(task)
