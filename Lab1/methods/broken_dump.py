from methods.base import frange

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
from plotly.graph_objs import *

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
    #Incorrect way to evaluate L 
    #\_/
    #L = (function(a+step)-function(a))/step
    #for i in range(1,subdivision):
    #    tmp = (function(a+step*(i+1))-function(a+step*i))/step
    #    L = tmp if abs(tmp) > abs(L) else L
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

    index = 1
    x = [[a,function(a),0],[x0,y0,1],[b,function(b),0]]

    dumpArray = [[[y for y in xx] for xx in x]]

    while True:
        itter += 1
        d = (function(x0)-y0)/(2*L)

        #print(d,x)

        if abs(2*d*L) < epsilon:
            return x0, function(x0), itter, dumpArray

        x1 = x0 - d
        x2 = x0 + d
        
        x[index][2] = 0
        x.insert(index+1,[x2,(function(x0) + y0)/2,1])
        x.insert(index,[x1,(function(x0) + y0)/2,1])

        dumpArray.append([[y for y in xx] for xx in x])
        #if itter > 20:
        #    print('[ASSERT] Failsafe')
        #    print(x)
        #    return None

        if x[index][2] == 0:
            print('[ASSERT] Incorrect index')
            return None

        index = index
        minX = function(x[index][0])
        x0 = x[index][0]
        y0 = x[index][1]

        for i in range(len(x)):
            if function(x[i][0]) < minX and x[i][2] == 1:
                minX = function(x[i][0])
                x0 = x[i][0]
                y0 = x[i][1]
                index = i

def plotDump(task,dump,name='dump.html'):
    function = task.function

    fig = Figure()

    xVar = frange(*task.xRange, task.epsilon)
    yVar = [function(x) for x in xVar]
    fig.add_trace( Scatter(x = xVar, y = yVar, name = 'Our function') )

    for data in dump:
        xVar = [x[0] for x in data]
        yVar = [x[1] if x[2] == 1 else function(x[0]) for x in data]
        scat = Scatter(x = xVar, y = yVar, name=f'Iteration:{dump.index(data)}')
        fig.add_trace( scat )

    steps = []

    for i in range(1,len(fig.data)):
        step = dict(
            method="restyle",
            args=[  {"visible": [True] * (i+1) + [False] * (len(fig.data)-i-1), "line": [dict(dash='dash',width=1) if j!=0 and j!=i else dict(dash='solid',width=2) for j in range(i)] }   ]
        )
        #step['args'][1]['line.dash'][i] = 'solid'
        steps.append(step)

    sliders = [dict(
        active=len(fig.data)-2,
        currentvalue={"prefix": "Iterations: "},
        pad={"t": len(fig.data)-1},
        steps=steps 
        )]
    
    fig.update_layout(
        sliders=sliders
    )

    fig.show()
    #plot(output,filename = name,show_link=False)
