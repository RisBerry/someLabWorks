from methods import base,bruteforce,decimal,dyhotomy,golden,parabolla,midpoint,chord,newton,markwardt,newton_rafson
from methods.base import timeIt,frange
from math import *
import gc

gc.disable()

def taskFunc(x):
    y = x * atan(x) - log(1+x*x)/2 
    return y

def diff1F(x):
    y = atan(x)
    return y

def diff2F(x):
    y = 1/(1+x*x)
    return y

myTask = base.task(taskFunc, [-1.9, 1.9], 0.001, diff1F, diff2F)

base.plotFunction(myTask, name = 'atan.html')

myTask.xRange = [-1., 1.]

timeIt(bruteforce,myTask)
timeIt(decimal,myTask)
timeIt(dyhotomy,myTask)
timeIt(golden,myTask)
timeIt(parabolla,myTask,seq=1) #Failed division by zero
timeIt(midpoint,myTask)
timeIt(chord,myTask)
print('\n#Test newton and modifications')
timeIt(newton,myTask)
timeIt(markwardt,myTask)
timeIt(newton_rafson,myTask)

print('\n#Test with unoptimal range')

myTask.xRange = [-1.5, 1.5]

timeIt(newton,myTask,seq=1)
timeIt(markwardt,myTask)
timeIt(newton_rafson,myTask)
