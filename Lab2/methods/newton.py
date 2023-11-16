import methods.decimal as decimal
import methods.matrix as matrix
import methods.vector as vec
from math import sqrt
from math import isnan

def calculate(task):

    func = task.func
    xk = task.startpoint
    e = task.epsilon
    e1d = task.epsilon1d


    while True:
        if isnan(xk[0]):
            print(f'[ASSERT | {__name__}] NaN detected')
            return None

        grad = func.grad(*xk)
        if vec.vlen(grad) < e:
            z = func.get(*xk)
            return (*xk , z)

        hess = matrix.invert(func.hess(*xk))

        if hess is None:
            print(f'[ASSERT | {__name__}] Determinat is zero')
            return None

        grad = func.grad(*xk)

        tmpX = hess[0][0]*grad[0] + hess[0][1]*grad[1]
        tmpY = hess[1][1]*grad[1] + hess[1][0]*grad[0]
        tmp = (tmpX,tmpY)

        xk = vec.sub(xk,tmp)
