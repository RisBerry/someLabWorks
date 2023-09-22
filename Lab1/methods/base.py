from time import perf_counter_ns as time 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
from plotly.graph_objs import *
import gc

class task:
    function = None
    diff1= None
    diff2= None
    epsilon = 1.
    xRange = [-1.,1.] 

    def __init__(self, function, xRange, epsilon, diff1 = None, diff2 = None):
        self.function = function
        self.xRange = xRange
        self.epsilon = epsilon
        self.diff1 = diff1
        self.diff2 = diff2

def timeIt(calculusClass,task,seq=100):
    #gc.disable()
    SeqLaunches = seq 

    timeStart = time()
    [calculusClass.calculate(task) for i in range(SeqLaunches-1)]
    result = calculusClass.calculate(task)
    endTime = time() - timeStart
    #gc.enable()
    #gc.collect()
    if result is None:
        return
    print(f'Execution time of {calculusClass.__name__:24s} is {endTime/SeqLaunches/1000:9.3f} us. X: {result[0]:10.7f} Y: {result[1]:10.10f}')

def frange(start,stop,step):
    out = []
    while start<=stop:
        out.append(start)
        start+=step
    return out

def plotFunction(task, name = 'plot.html'):
    xVar = frange(*task.xRange, task.epsilon)
    yVar = [task.function(x) for x in xVar]
    output = [Scatter(x = xVar, y = yVar, name = 'Our function')]
    plot(output,filename = name,show_link=False)
