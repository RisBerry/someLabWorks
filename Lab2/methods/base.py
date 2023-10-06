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
    dX1 = None
    dX2 = None

    countCalls = 0
    countDeriv = 0

    def __init__(self, func, diffX1, diffX2):
        self.func = func
        self.dX1 = diffX1
        self.dX2 = diffX2

    def reset(self):
        self.countCalls = 0
        self.countDeriv = 0

        if isinstance(self.dX1, type(self)):
            return self.dX1.reset()

        if isinstance(self.dX2, type(self)):
            return self.dX2.reset()

    def get(self,x,y):
        self.countCalls+=1
        return self.func(x, y)

    def get_dX1(self,x,y):
        if isinstance(self.dX1, type(self)):
            return self.dX1.get(x, y)
        else:
            self.countDeriv+=1
            return self.dX1(x, y)

    def get_dX2(self,x,y):
        if isinstance(self.dX2, type(self)):
            return self.dX2.get(x, y)
        else:
            self.countDeriv+=1
            return self.dX2(x, y)

    def callCount(self):
        func  = self.countCalls
        deriv = self.countDeriv

        if isinstance(self.dX1, type(self)):
            deriv += sum(self.dX1.callCount())

        if isinstance(self.dX2, type(self)):
            deriv += sum(self.dX2.callCount())

        return (func, deriv)

class task:
    func = None
    startpoint = None
    epsilon = 1.

    def __init__(self, function, epsilon, startpoint = (.0, .0)):
        self.func = function
        self.epsilon = epsilon
        self.startpoint = startpoint
    
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

    result = calculusClass.calculate(task)
    
    if result is None:
        return
    print(f'Total calls: {task.totalCallCount} Func calls: {task.functionCallCount} Deriv calls: {task.derivCallCount} | X: 0.0 Y: 0.0 Z: 0.0')

def frange(start,stop,step):
    out = []
    while start<=stop:
        out.append(start)
        start+=step
    return out

def plotFunction(task, rad, name = 'plot.html'):
    if not plotlyInstalled:
        print('[ERROR] No plotly installed | Aborting graph plotting')
        return
    x,y = task.startpoint
    e = task.epsilon
    xVar = frange(x-rad,x+rad,e)
    yVar = frange(y-rad,y+rad,e)
    zVar = [[task.func.get(x,y) for x in xVar] for y in yVar]
    output = [Surface(x = xVar, y = yVar, z = zVar, name = 'Our function')]
    plot(output,filename = name,show_link=False)
