from methods import base,bruteforce,broken,broken_dump
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

task1 = base.task(taskFunc1, [1., 12.], 0.01)
task2 = base.task(taskFunc2, [0., 4.], 0.01)

#base.plotFunction(task1, name = 'cos_x.html')
#base.plotFunction(task2, name = 'X_2sin.html')

print('#Launching task1')
timeIt(bruteforce,task1)
timeIt(broken,task1)
timeIt(broken_dump,task1)

dump = broken_dump.calculate(task1)[3]
broken_dump.plotDump(task1,dump)

print('\n#Launching task2')
timeIt(bruteforce,task2)
timeIt(broken,task2)
timeIt(broken_dump,task2)

dump = broken_dump.calculate(task2)[3]
broken_dump.plotDump(task2,dump,name='dump2.html')
