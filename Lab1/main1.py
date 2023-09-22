from methods import base,bruteforce,decimal,dyhotomy,golden,parabolla,midpoint,chord,newton
from methods.base import timeIt,frange
from math import *
import gc

gc.disable()

def taskFunc(x):
    y = x*sin(x)+2*cos(x) 
    return y

def diff1F(x):
    y = x*cos(x)-sin(x)
    return y

def diff2F(x):
    y = -x*sin(x)
    return y

myTask = base.task(taskFunc, [-6., -4.], 0.0001, diff1F, diff2F)

base.plotFunction(myTask)

timeIt(bruteforce,myTask)
timeIt(decimal,myTask)
timeIt(dyhotomy,myTask)
timeIt(golden,myTask)
timeIt(parabolla,myTask)
timeIt(midpoint,myTask)
timeIt(chord,myTask)
timeIt(newton,myTask)
