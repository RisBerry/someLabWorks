from methods import base,bruteforce,broken
from methods.base import timeIt
from math import *
import gc

gc.disable()

def taskFunc1(x):
    y = cos(x)/(x*x) 
    return y

def taskFunc2(x):
    y = x/10. + 2*sin(4*x) 
    return y

task1 = base.task(taskFunc1, [1., 12.], 0.001)
task2 = base.task(taskFunc2, [0., 4.], 0.001)

#base.plotFunction(task1, name = 'cos_x.html')
#base.plotFunction(task2, name = 'X_2sin.html')

print('#Launching task1')
timeIt(bruteforce,task1)
timeIt(broken,task1,seq=1)

print('\n#Launching task2')
timeIt(bruteforce,task2)
#timeIt(broken,task2)
