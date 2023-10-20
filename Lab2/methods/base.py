#from time import perf_counter_ns as time 
try:
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
    import plotly
    from plotly.graph_objs import *
    plotlyInstalled = True
except:
    print('[WARNING] Plotly not installed. Graph plotting will not work')
    plotlyInstalled = False


class function:
    func = None
    dX = None
    dY = None

    countCalls = 0
    countDeriv = 0

    def __init__(self, func, diffX, diffY):
        self.func = func
        self.dX = diffX
        self.dY = diffY

    def reset(self):
        self.countCalls = 0
        self.countDeriv = 0

        if isinstance(self.dX, type(self)):
            self.dX.reset()

        if isinstance(self.dY, type(self)):
            self.dY.reset()

    def hess(self, x, y):
        return [
            [self.dX.get_dX(x, y), self.dX.get_dY(x, y)],
            [self.dY.get_dX(x, y), self.dY.get_dY(x, y)]
                ]
    
    def grad(self, x, y):
        return [self.get_dX(x, y), self.get_dY(x, y)]

    def get(self,x,y):
        self.countCalls+=1
        return self.func(x, y)

    def get_dX(self,x,y):
        if isinstance(self.dX, type(self)):
            return self.dX.get(x, y)
        else:
            self.countDeriv+=1
            return self.dX(x, y)

    def get_dY(self,x,y):
        if isinstance(self.dY, type(self)):
            return self.dY.get(x, y)
        else:
            self.countDeriv+=1
            return self.dY(x, y)

    def callCount(self):
        func  = self.countCalls
        deriv = self.countDeriv

        if isinstance(self.dX, type(self)):
            deriv += sum(self.dX.callCount())

        if isinstance(self.dY, type(self)):
            deriv += sum(self.dY.callCount())

        return (func, deriv)

class task:
    func = None
    startpoint = None
    epsilon = 1.
    epsilon1d = 1.

    def __init__(self, function, epsilon, startpoint = (.0, .0), epsilon1d = None):
        self.func = function
        self.epsilon = epsilon
        self.startpoint = startpoint
        if epsilon1d is None:
            self.epsilon1d = epsilon
        else:
            self.epsilon1d = epsilon1d
    
    def reset(self):
        self.func.reset()

    def derivCallCount(self):
        return self.func.callCount()[1]

    def functionCallCount(self):
        return self.func.callCount()[0]

    def totalCallCount(self):
        return sum(self.func.callCount())

############################################

def timeIt(calculusClass,task):

    task.reset()

    result = calculusClass.calculate(task)
    
    if result is None:
        print(f'[ASSERT | {calculusClass.__name__}] Calculation returned None')
        return

    x,y,z = result
    print(f'[{calculusClass.__name__:20s}] Total calls: {task.totalCallCount():7d} Func calls: {task.functionCallCount():7d} Deriv calls: {task.derivCallCount():7d} | X: {x:.6f} Y: {y:.6f} Z: {z:.6f}')

def frange(start,stop,step):
    out = []
    while start<=stop:
        out.append(start)
        start+=step
    return out

def plotFunction(func, start, e, rad, name = 'plot.html'):
    x,y = start
    xVar = frange(x-rad,x+rad,e)
    yVar = frange(y-rad,y+rad,e)
    zVar = [[func.get(x,y) for x in xVar] for y in yVar]
    output = [Surface(x = xVar, y = yVar, z = zVar, name = 'Our function')]
    plot(output,filename = name,show_link=False)

def plotTask(task, rad, name = 'plot.html'):
    if not plotlyInstalled:
        print('[ERROR] No plotly installed | Aborting graph plotting')
        return
    plotFunction(task.func, task.startpoint, task.epsilon, rad, name)
