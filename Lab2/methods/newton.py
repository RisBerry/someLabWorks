import methods.decimal as decimal
import methods.matrix as matrix
import methods.vector as vec
from math import sqrt

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

        hess = matrix.invert(func.hess(*xk))
        grad = func.grad(*xk)

        tmp = vec.mulV(grad, (hess[0][0],hess[1][1]))

        xk = vec.sub(xk,tmp)
