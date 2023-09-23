from methods.base import frange

def calculate(task):
    a = task.xRange[0]
    b = task.xRange[1]
    epsilon = task.epsilon

    function = task.function
    
    answer = None

    sigma = epsilon * .2
    #sigma = .0

    x1 = None
    x2 = None
    f1 = None
    f2 = None

    itter = 0

    while True:
        itter += 1

        if (b-a)/2 < epsilon:
            return (a+b)/2, function((a+b)/2), itter
        x1 = (b+a-sigma)/2
        x2 = (b+a+sigma)/2

        f1 = function(x1)
        f2 = function(x2)

        if f1<=f2:
            b=x2
        else:
            a=x1
