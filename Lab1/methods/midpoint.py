from methods.base import frange

def calculate(task):
    a = task.xRange[0]
    b = task.xRange[1]
    epsilon = task.epsilon

    function = task.function

    diff = task.diff1

    if diff is None:
        print(f'[ASSERT|{__name__}] First diff function is not available')
        return None
    
    itter = 0
    xPrev = None

    while True:
        itter += 1

        xm = (a+b)/2
        fm = diff(xm)

        if xPrev is not None and abs(xm - xPrev) <= epsilon:
            return xm, function(xm), itter

        xPrev = xm 
        if fm > 0:
            b = xm
        else:
            x0 = a
            a = xm
