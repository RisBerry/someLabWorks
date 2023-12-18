#from time import perf_counter_ns as time 
from math import sqrt
from copy import deepcopy
try:
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
    import plotly
    from plotly.graph_objs import *
    plotlyInstalled = True
except:
    print('[WARNING] Plotly not installed. Graph plotting will not work')
    plotlyInstalled = False


class function:
    buf = None
    viewed = None

    #Hardcoded values for test files
    startPoint = (50. , -3950.)
    step = 100.
    dimensionSize = 40

    inverted = False

    def __init__(self, filePath):
        #Uniform reading (hardcoded to 40x40 with uniform step)
        f = open(filePath)

        array = []
        for line in f:
            if len(line.split()) != 3:
                continue
            x,y,z = map(float, line.split())
            array.append([x,y,z])

        values =      [[ None for j in range(self.dimensionSize)] for i in range(self.dimensionSize)]
        self.viewed = [[False for j in range(self.dimensionSize)] for i in range(self.dimensionSize)]

        for i in array:
            x,y,z = i
            x = int((x - self.startPoint[0])/self.step)
            y = int((y - self.startPoint[1])/self.step)
            values[x][y] = z

        self.buf = values

    def indexToCords(self,i,j):
        i,j = self.restrict(i,j)
        x = self.startPoint[0] + self.step*i
        y = self.startPoint[1] + self.step*j
        return (x,y)

    def reset(self):
        l = len(self.viewed)
        self.viewed = [[False for j in range(l)] for i in range(l)]

    def isVisited(x,y):
        return self.viewed[x][y]

    def get(self,x,y):
        x,y = self.restrict(x,y)
        self.viewed[x][y] = True
        return -self.buf[x][y] if self.inverted else self.buf[x][y] 

    def restrict(self,i,j):
        i = int(min(max(i,0),self.dimensionSize-1))
        j = int(min(max(j,0),self.dimensionSize-1))
        return (i,j)

    def callCount(self):
        return sum([sum(i) for i in self.viewed])

class task:
    func = None
    trace = None
    basepoint = (0 , 0)
    itter = 0

    value = None

    def __init__(self, fileName):
        self.func = function(fileName)

    def getValue(self):
        self.value = min([min([self.func.get(i,j) for j in range(40)]) for i in range(40)])

    def setInverted(self, value):
        self.func.inverted = value
        self.getValue()

    def addTraceConverted(self,i,j):
        x,y = self.func.indexToCords(i,j)
        self.trace.append((x,y))

    def addTrace(self,x,y):
        self.trace.append((x,y))

    def reset(self):
        self.trace = []
        self.itter = 0
        self.func.reset()

    def callCount(self):
        return self.func.callCount()

############################################
def genPoints(seed, N = 100):
    import random

    random.seed(seed)

    allPoints = [[i%40,i//40] for i in range(1600)]

    return random.sample(allPoints, N)

def avg(array):
    return sum(array)/len(array)

def reportIt(calculusClass,task,points):

    results = []

    N = len(points)
    S = 0

    itter = 0
    callCount = 0

    goodTrace = None

    for point in points:
        task.basepoint = point
        task.reset()

        results.append(calculusClass.calculate(task))

        itter = max(itter, task.itter)
        callCount = max(task.callCount(), callCount)

        if results[-1][2] == task.value:
            if goodTrace is None:
                goodTrace = deepcopy(task.trace)
            S += 1
    
    z = [-z[2] if task.func.inverted else z[2] for z in results]

    print(f'[{calculusClass.__name__:20s}] Max file reads: {callCount:4d} | Max itterations: {itter:4d} | minZ: {min(z):.6f} maxZ: {max(z):.6f} avgZ: {avg(z):.6f} | Success rate: {100*S/N:.2f}%')
    #plotTrace(task, None, None, trace = goodTrace)
    #plotScatter(task, results)

def plot1dParam(task, calcClass, param = None, points = None):
    if param is None:
        return

    if not plotlyInstalled:
        print('[ERROR] No plotly installed | Aborting graph plotting')
        return

    p0 = param

    from math import ceil
    p0s = p0[1]
    p0p = p0[3]
    p0i = ceil((p0[2] - p0[1])/p0[3]) + 1

    results = [None for i in range(p0i)]

    for i in range(p0i):
        #print(i,j)
        p0[0](p0s+p0p*i)

        N = len(points)
        S = 0

        for point in points:
            task.basepoint = point
            task.reset()

            result = calcClass.calculate(task)

            if result[2] == task.value:
                S += 1
        results[i] = 100*S/N
        #print(calcClass.L,calcClass.a,results[i][j])

    xVar = [p0s+p0p*i for i in range(p0i)]
    h = Scatter(x = xVar, y = results, mode='markers' ,name = 'Probabilitis')
    fig = Figure()
    fig.add_trace(h)
    fig.update_yaxes(range=(0,100))
    #fig.write_html(name)
    fig.show()

def plot2dParam(task, calcClass, params = None, points = None):
    if params is None:
        return

    if not plotlyInstalled:
        print('[ERROR] No plotly installed | Aborting graph plotting')
        return

    p0 = params[0]
    p1 = params[1]

    p0s = p0[1]
    p1s = p1[1]

    p0p = p0[3]
    p1p = p1[3]

    from math import ceil
    p0i = ceil((p0[2] - p0[1])/p0[3]) + 1
    p1i = ceil((p1[2] - p1[1])/p1[3]) + 1

    results = [[None for j in range(p1i)] for i in range(p0i)]

    for i in range(p0i):
        #print(f'{i} out of {p0i}')
        for j in range(p1i):
            #print(i,j)
            p0[0](p0s+p0p*i)
            p1[0](p1s+p1p*j)

            N = len(points)
            S = 0

            for point in points:
                task.basepoint = point
                task.reset()

                result = calcClass.calculate(task)

                if result[2] == task.value:
                    S += 1
            results[i][j] = 100*S/N
            #print(calcClass.L,calcClass.a,results[i][j])

    yVar = [p0s+p0p*i for i in range(p0i)]
    xVar = [p1s+p1p*i for i in range(p1i)]
    h = Heatmap(x = xVar, y = yVar, z = results, name = 'Probabilitis', zmin = 0, zmax = 100)
    fig = Figure()
    fig.add_trace(h)
    #fig.write_html(name)
    fig.show()

def plotTrace(task, calcClass, startPoint = (0,0),trace = None, name = 'trace.html'):
    if not plotlyInstalled:
        print('[ERROR] No plotly installed | Aborting graph plotting')
        return

    if trace is None:
        task.basepoint = startPoint 
        task.reset()
        calcClass.calculate(task)

        trace = task.trace

    x = [p[0] for p in trace]
    y = [p[1] for p in trace]

    output = [Scatter(x = x, y = y, name = 'Trace route'), getHeatmap(task)]
    fig = Figure()
    fig.add_traces(output)
    fig.update_xaxes(range=(0,4000))
    fig.update_yaxes(range=(-4000,-0))
    #fig.write_html(name)
    fig.show()
    #plot(output,filename = name,show_link=False)

def plotScatter(task, trace, name = 'trace.html'):
    if not plotlyInstalled:
        print('[ERROR] No plotly installed | Aborting graph plotting')
        return

    x = [p[0] for p in trace]
    y = [p[1] for p in trace]

    output = [Scatter(x = x, y = y, name = 'All results',mode='markers'), getHeatmap(task)]
    fig = Figure()
    fig.add_traces(output)
    fig.update_xaxes(range=(0,4000))
    fig.update_yaxes(range=(-4000,-0))
    #fig.write_html(name)
    fig.show()
    #plot(output,filename = name,show_link=False)

def getHeatmap(task):
    xVar = [task.func.startPoint[0] + task.func.step*i for i in range(40)]
    yVar = [task.func.startPoint[1] + task.func.step*i for i in range(40)]
    zVar = [[task.func.get(x,y) * (-1 if task.func.inverted else 1) for x in range(40)] for y in range(40)]
    return Heatmap(x = xVar, y = yVar, z = zVar, name = 'Our function')

def plotFunction(task, name = 'plot.html'):
    if not plotlyInstalled:
        print('[ERROR] No plotly installed | Aborting graph plotting')
        return

    xVar = [task.func.startPoint[0] + task.func.step*i for i in range(40)]
    yVar = [task.func.startPoint[1] + task.func.step*i for i in range(40)]
    zVar = [[task.func.get(x,y) for x in range(40)] for y in range(40)]
    output = [Surface(x = xVar, y = yVar, z = zVar, name = 'Our function')]
    plot(output,filename = name,show_link=False)
