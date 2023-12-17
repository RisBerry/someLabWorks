import methods.vector as v
import random

N = 40
L = 10
a = 2

#To have determenistic results
seed = 1234

def setL(x):
    global L
    L = x

def seta(x):
    global a
    a = x

def setN(x):
    global N
    N = x

def calculate(task):
    task.reset()

    func = task.func
    size = func.dimensionSize

    startPoint = task.basepoint

    bestPoint = func.get(*startPoint) 
    cords = startPoint

    lVector = L

    random.seed(1234)

    while True:
        task.itter += 1
        task.addTraceConverted(*cords)

        if lVector < 1:
            return (*func.indexToCords(*cords),bestPoint)

        #Generate vectors
        baseVectors = []
        for i in range(N):
            vec = None
            while True:
                vec = v.normalize((random.random()*2-1,random.random()*2-1))
                if vec in baseVectors:
                    continue
                break
            baseVectors.append(vec) 


        vector = baseVectors[0]
        point = func.get(*v.add(cords,v.mulC(vector,lVector)))
        for vec in baseVectors[1:]:
            c = v.add(cords,v.mulC(vec,lVector))
            p = func.get(*c)
            if p < point:
                point = p
                vector = vec

        if point < bestPoint:
            bestPoint = point
            cords = v.add(cords,v.mulC(vector,lVector))
        else:
            lVector /= a
