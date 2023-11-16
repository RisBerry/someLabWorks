import methods.decimal as decimal
import methods.vector as vec
from math import sqrt

vanilla = True
alternativeVectors = False
step = 10

def calculate(task):

    func = task.func
    xk = task.startpoint
    e = task.epsilon
    e1d = task.epsilon1d

    if alternativeVectors:
        basevectors = [
            (1.,1.),
            (-1.,1.),
                ]
    else:
        basevectors = [
            (1.,0.),
            (0.,1.),
                ]
    for bv in basevectors:
        bv = vec.normalize(bv)

    currentVector = 0
    grad = None

    while True:

        #Condition described below. Doesn't work properly on this method
        #print(xk,grad)
        if not vanilla:
            grad = func.grad(*xk)
        #if vec.vlen(grad) < e:
        #    z = func.get(*xk)
        #    return (*xk , z)

        z = func.get(*xk)

        if not vanilla:
            a = max(e, abs(grad[currentVector]))
        bv = basevectors[currentVector]

        func1d = lambda ak: func.get(*vec.add(xk, vec.mulC(c = ak, v = bv) ))
        if vanilla:
            a = decimal.calculate(func1d, -step, step, e1d)
        else:
            a = decimal.calculate(func1d, -a, a, e1d)
        xk = vec.add(xk, vec.mulC(c = a, v = bv) )

        currentVector = (currentVector + 1) % len(basevectors)

        #Using alternative method
        zn = func.get(*xk)
        if abs(z-zn) < e:
            return (*xk , zn)
