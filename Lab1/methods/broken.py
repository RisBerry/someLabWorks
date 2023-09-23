from methods.base import frange

def calcL(task):
    #Consts
    #subdivision = 10
    subdivision = 100
    #subdivision = 1000
    correction = 1
    #correction = 1.5
    #correction = 10 #Good for first task
    ######
    a = task.xRange[0]
    b = task.xRange[1]
    function = task.function

    step = (b-a)/subdivision
    L = abs((function(a+step)-function(a))/step)
    for i in range(1,subdivision):
        tmp = abs((function(a+step*(i+1))-function(a+step*i))/step)
        L = tmp if tmp > L else L
    return L*correction


def calculate(task):
    a = task.xRange[0]
    b = task.xRange[1]
    epsilon = task.epsilon
    function = task.function

    L = calcL(task)
    #print('L:',L)

    x0 = (function(a)-function(b)+L*(a+b))/(2*L)
    y0 = (function(a)+function(b)+L*(a-b))/(2)

    itter = 0

    index = 0
    x = [[x0,y0]]

    while True:
        itter += 1
        d = (function(x0)-y0)/(2*L)

        #print(d,x)

        if abs(2*d*L) < epsilon:
            return x0, function(x0), itter

        x1 = x0 - d
        x2 = x0 + d
        x.pop(index)
        x.append([x1,y0])
        x.append([x2,y0])
        #print(L,d,x0,y0,x1,x2)
        index = 0
        minX = function(x[0][0])
        for i in range(len(x)):
            if function(x[i][0]) < minX:
                minX = function(x[i][0])
                y0 = x[i][1]
                index = i

        y0 = (function(x0) + y0)/2
        x0 = x[index][0]
