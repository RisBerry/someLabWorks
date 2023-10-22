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
cycle.vanilla = True
cycle.step = 3
hj.vanilla = False
hj.step = 1
hj.gamma =  2
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
        lambda x,y : , #Func
        lambda x,y : , #Deriv1
        lambda x,y :  #Deriv2
        )
derivY = base.function(
        lambda x,y : , #Func
        lambda x,y : , #Deriv1
        lambda x,y :   #Deriv2
        )
func   = base.function(
        lambda x,y : (x**2+y-11)**2+(x+y**2-7)**2,
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
