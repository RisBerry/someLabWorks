from methods import base
from methods import bruteforce,template,random
from methods.base import reportIt

fileName = 'data\Функция_П2.txt'

findMax = False 

#Tuning
if findMax:
    template.L = 11
    template.a = 1.1

    random.N = 16
    random.L = 15 
    random.a = 1.25
else:
    template.L = 28
    template.a = 1.1

    random.N = 16
    random.L = 25
    random.a = 1.25

task = base.task(fileName)
task.reset()

task.setInverted(findMax)

#generate start points
points = base.genPoints(1111)
smallPoints = base.genPoints(2222, N = 40)

#base.plotFunction(task)

#reportIt(bruteforce,task,points)

#reportIt(template,task,points)
#base.plot2dParam(task,template, [(lambda x:template.setL(x),1,30,1),(lambda x:template.seta(x),1.1,2.,0.05)], smallPoints)

#reportIt(random,task,points)
#base.plot2dParam(task,random, [(lambda x:random.setL(x),1,30,1),(lambda x:random.seta(x),1.1,2.,0.05)], smallPoints)
#base.plot1dParam(task,random, (lambda x:random.setN(x),1,100,1), smallPoints)
