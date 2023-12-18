import methods.vector as v

L = 10
a = 2

def setL(x):
    global L
    L = x

def seta(x):
    global a
    a = x

def calculate(task):
    task.reset()

    func = task.func
    size = func.dimensionSize

    startPoint = task.basepoint

    bestPoint = func.get(*startPoint) 
    cords = startPoint

    lVector = L

    baseVectors = [
            (-1, 0),
            ( 1, 0),
            ( 0,-1),
            ( 0, 1),
            ( 1, 1),
            ( 1,-1),
            (-1, 1),
            (-1,-1),
            ]

    while True:
        task.addTraceConverted(*cords)

        if lVector < 1:
            return (*func.indexToCords(*cords),bestPoint)

        task.itter += 1

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
            #Restrict
            cords = func.restrict(*cords)
        else:
            lVector /= a
