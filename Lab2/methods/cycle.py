import methods.decimal as decimal
import methods.vector as vec
from math import sqrt

def calculate(task):

    func = task.func
    xk = task.startpoint
    e = task.epsilon
    e1d = task.epsilon1d

    basevectors = (
        (1.,0.),
        (0.,1.),
            )

    currentVector = 0

    while True:

        #Condition described below. Doesn't work properly on this method
        #print(xk,grad)
        grad = func.grad(*xk)
        #if vec.vlen(grad) < e:
        #    z = func.get(*xk)
        #    return (*xk , z)

        z = func.get(*xk)

        a = max(e, abs(grad[currentVector]))
        bv = basevectors[currentVector]

        func1d = lambda ak: func.get(*vec.add(xk, vec.mulC(c = ak, v = bv) ))
        a = decimal.calculate(func1d, -a, a, e1d)
        xk = vec.add(xk, vec.mulC(c = a, v = bv) )

        currentVector = (currentVector + 1) % len(basevectors)

        #Using alternative method
        zn = func.get(*xk)
        if abs(z-zn) < e:
            return (*xk , zn)
