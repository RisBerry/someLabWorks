from methods import base
from methods.base import timeIt
from math import *
import gc

gc.disable()

a1derivX = base.function(
        lambda x,y : 2*x, #Func
        lambda x,y : 2  , #Deriv1
        lambda x,y : 0    #Deriv2
        )
a1derivY = base.function(
        lambda x,y :    1*2*y, #Func
        lambda x,y :    0    , #Deriv1
        lambda x,y :    1*2    #Deriv2
        )
a1func   = base.function(
        lambda x,y : x**2 +    1 * y**2,
        a1derivX,
        a1derivY
        )

taskA1 = base.task(a1func, .1, startpoint = (.0, .0))

#print('\nEpsilon: 0.1')

#base.plotTask(taskA1, 10)
#timeIt(bruteforce,myTask)
