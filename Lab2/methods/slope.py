import methods.decimal as decimal
import methods.vector as vec
from math import sqrt

vanilla = False
minDist = 100
correction = 2.

def calculate(task):

    func = task.func
    xk = task.startpoint
    e = task.epsilon
    e1d = task.epsilon1d

    while True:
        grad = func.grad(*xk)
        if vec.vlen(grad) < e:
            z = func.get(*xk)
            return (*xk , z)

        norm = vec.normalize(grad)
 
        if vanilla:
            a = max(minDist, vec.vlen(grad)*correction)
            func1d = lambda ak: func.get(*vec.sub(xk, vec.mulC(c = ak, v = grad) ))
            a = decimal.calculate(func1d, 0, a, e1d)
            xk = vec.sub(xk, vec.mulC(c = a, v = grad) )
        else:
            a = max(e, vec.vlen(grad)*correction)
            if a > 1:
                func1d = lambda ak: func.get(*vec.sub(xk, vec.mulC(c = ak, v = norm) ))
                a = decimal.calculate(func1d, 0, a, e1d)
                xk = vec.sub(xk, vec.mulC(c = a, v = norm) )
            else:
                a = sqrt(a)
                func1d = lambda ak: func.get(*vec.sub(xk, vec.mulC(c = ak, v = grad) ))
                a = decimal.calculate(func1d, e1d/2., a, e1d)
                xk = vec.sub(xk, vec.mulC(c = a, v = grad) )
        #print(a,xk,vec.vlen(grad),grad,norm)
