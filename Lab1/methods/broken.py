from methods.base import frange

def calcL(task):
    #Consts
    #subdivision = 10
    subdivision = 20
    #subdivision = 1000
    correction = 1
    #correction = 1.5
    #correction = 10 #Good for first task
    ######
    a = task.xRange[0]
    b = task.xRange[1]
    function = task.function

    step = (b-a)/subdivision
    L = (function(a+step)-function(a))/step
    for i in range(1,subdivision):
        tmp = (function(a+step*(i+1))-function(a+step*i))/step
        L = max(tmp,L)
    return L*correction


def calculate(task):
    a = task.xRange[0]
    b = task.xRange[1]
    epsilon = task.epsilon
    function = task.function

    L = calcL(task)
    #print(L)

    x0 = (function(a)-function(b)+L*(a+b))/(2*L)
    y0 = (function(a)+function(b)+L*(a-b))/(2)

    while True:
        d = (function(x0)-y0)/(2*L)

        if abs(2*d*L) < epsilon:
            return x0, function(x0)

        x1 = x0 - d
        x2 = x0 + d
        #print(L,d,x0,y0,x1,x2)

        if function(x1) < function(x2):
            x0 = x1
        else:
            x0 = x2

        y0 = (function(x0) + y0)/2
