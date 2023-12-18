from methods import base
from methods import bruteforce,template,random,heating,genetic
from methods.base import reportIt

fileName = 'data\Функция_П4_В3.txt'

findMax = False

#Tuning
if findMax:
    template.L = 26
    template.a = 1.3

    random.N = 60
    random.L = 26 
    random.a = 1.1

    heating.a = 0.99
    heating.L = 11
    heating.T = 100
    heating.Tstop = 0.0001

    genetic.a = 0.35
    genetic.b = 0.45
    genetic.N = 55
    genetic.maxItter = 55
else:
    template.L = 27
    template.a = 1.5

    random.N = 35
    random.L = 27
    random.a = 1.35

    heating.a = 0.97
    heating.L = 9
    heating.T = 105
    heating.Tstop = 0.0001

    genetic.a = 0.35
    genetic.b = 0.5
    genetic.N = 70
    genetic.maxItter = 55

task = base.task(fileName)
task.reset()

task.setInverted(findMax)

#generate start points
points = base.genPoints(1111)
smallPoints = base.genPoints(2222, N = 40)

#base.plotFunction(task)

reportIt(bruteforce,task,points)

reportIt(template,task,points)
#base.plot2dParam(task,template, [(lambda x:template.setL(x),1,30,1),(lambda x:template.seta(x),1.1,2.,0.05)], smallPoints)

reportIt(random,task,points)
#random.N = 32
#base.plot2dParam(task,random, [(lambda x:random.setL(x),1,30,1),(lambda x:random.seta(x),1.1,2.,0.05)], smallPoints)
#base.plot1dParam(task,random, (lambda x:random.setN(x),1,100,1), smallPoints)

reportIt(heating,task,points)
#heating.T = 100
#heating.Tstop = 0.001
#base.plot2dParam(task,heating, [(lambda x:heating.setL(x),1,20,1),(lambda x:heating.seta(x),0.8,0.99,0.005)], smallPoints)
#base.plot2dParam(task,heating, [(lambda x:heating.setT(x),50,200,5),(lambda x:heating.setTstop(x),0.0001,0.0101,0.001)], smallPoints)

reportIt(genetic,task,points)
#genetic.N = 50
#genetic.maxItter = 50 
#base.plot2dParam(task,genetic, [(lambda x:genetic.seta(x),0.1,0.9,0.05),(lambda x:genetic.setb(x),0.1,1.,0.05)], smallPoints)
#base.plot2dParam(task,genetic, [(lambda x:genetic.setN(x),10,100,5),(lambda x:genetic.setmaxItter(x),5,100,5)], smallPoints)
