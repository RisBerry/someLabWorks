from methods.base import frange

def calculate(task):
    a = task.xRange[0]
    b = task.xRange[1]
    epsilon = task.epsilon

    function = task.function
    diff = task.diff1

    dA = diff(a)
    dB = diff(b)

    xPrev = None
    itter = 0

    while True:
        itter += 1

        xm = a - (dA*(a-b))/(dA-dB)
        fm = diff(xm)

        if xPrev is not None and abs(xm - xPrev) <= epsilon:
            return xm, function(xm), itter
        
        xPrev = xm
        if fm > 0:
            b = xm
            dB = fm
        else:
            a = xm
            dA = fm
