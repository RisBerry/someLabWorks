from methods import base
from methods import slope,gradient,newton,simplex,cycle,hj,rnd
from methods.base import timeIt
from math import *

#import gc
#gc.disable()

#Default configuration
slope.vanilla = True
gradient.restart = 3
simplex.vanilla = True
simplex.l = 10
simplex.sigma = 0.2
cycle.vanilla = True
cycle.step = 20
hj.vanilla = True
hj.gamma = 10 
rnd.M = 100


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
        lambda x,y : 33+302*x-300*y, #Func
        lambda x,y : 302, #Deriv1
        lambda x,y : -300 #Deriv2
        )
derivY = base.function(
        lambda x,y : 99-300*x+302*y, #Func
        lambda x,y : -300 , #Deriv1
        lambda x,y : 302    #Deriv2
        )
func   = base.function(
        lambda x,y : 151*x**2-300*x*y+151*y**2+33*x+99*y+48,
        derivX,
        derivY
        )

task = base.task(func, .001, startpoint = (1., 1.))
task.epsilon1d = .00000001
#base.plotTask(task, 10)
massExec(task)

task.epsilon = .00001
#task.epsilon1d = .00001
massExec(task)
