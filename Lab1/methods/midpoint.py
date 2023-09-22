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
    
    while True:
        xm = (a+b)/2
        fm = diff(xm)

        if abs(fm) <= epsilon:
            return xm, function(xm)

        if fm > 0:
            b = xm
        else:
            a = xm

