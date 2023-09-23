from methods.base import frange
from math import sqrt

def calculate(task):
    a = task.xRange[0]
    b = task.xRange[1]
    epsilon = task.epsilon

    function = task.function
    
    answer = None
    
    t = (sqrt(5)-1)/2

    x1=a+(1-t)*(b-a)
    x2=a+t*(b-a)

    f1=function(x1)
    f2=function(x2)

    eps = (b-a)/2

    itter = 0
    
    while True:
        itter += 1

        if eps <= epsilon:
            xM = (b+a)/2.
            return xM, function(xM), itter

        if f1<=f2:
            b  = x2
            x2 = x1
            f2 = f1
            x1 = b-t*(b-a)
            f1 = function(x1)
        else:
            a  = x1
            x1 = x2
            f1 = f2
            x2 = b-(1-t)*(b-a)
            f2 = function(x2)

        eps *= t
