from methods.base import frange

def calculate(task):
    a = task.xRange[0]
    b = task.xRange[1]
    epsilon = task.epsilon

    function = task.function

    x1 = a + (b-a)*.25
    x2 = a + (b-a)*.50
    x3 = a + (b-a)*.75

    f1 = function(x1)
    f2 = function(x2)
    f3 = function(x3)

    xm, xmPrev = None, None

    #if f2 > f1 or f2 > f3:
    #    print('[ASSERT] Parabola cann\'t be applied')
    #    return None
    itter = 0

    while True:
        itter += 1
        if (x2-x1 == 0) or (x3-x2==0) or (x3-x1==0):
            print(f'[ASSERT|{__name__}] Parabola cann\'t be applied (division by zero)')
            return None

        a0 = f1
        a1 = (f2-f1)/(x2-x1)
        a2 = ((f3-f1)/(x3-x1) - (f2-f1)/(x2-x1))/(x3-x2)

        if a2==0:
            print(f'[ASSERT|{__name__}] Parabola cann\'t be applied (a2 is zero)')
            return None

        xm = (x1+x2-a1/a2)/2

        if xmPrev is not None and xm is not None and abs(xm-xmPrev) < epsilon:
            return xm, function(xm), itter 

        if   x1 <= xm <= x2:
            x3 = x2
            f3 = f2

            x2 = xm
            f2 = function(x2)
        elif x2 <= xm <= x3:
            x1 = x2
            f1 = f2

            x2 = xm
            f2 = function(x2)
        elif xm > x3:
            x1 = x2
            f1 = f2
            x2 = x3
            f2 = f3

            x3 = xm
            f3 = function(x3)
        elif xm < x1:
            x3 = x2 
            f3 = f2
            x2 = x1
            f2 = f1

            x1 = xm
            f1 = function(x1)
        #else:
        #    print('[ASSERT] Error during calculation:',x1,x2,x3,xm)
        #    return None

        xmPrev = xm

