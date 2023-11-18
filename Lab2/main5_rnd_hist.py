from methods import base
from methods import slope,gradient,newton,simplex,cycle,hj,rnd
from methods.base import timeIt
from math import *

#import gc
#gc.disable()

#Default configuration
slope.vanilla = False
gradient.restart = 3

simplex.vanilla = True
simplex.useGrad = False
simplex.l = 3
simplex.sigma = 0.85
simplex.alwaysDump = False
simplex.allPoints = False
simplex.allowTriangleFlip = True

cycle.vanilla = True
cycle.step = 3

newton.alwaysDump = False

hj.vanilla = False
hj.alternativeVectors = True
hj.step = 1
hj.gamma =  2

rnd.M = 200


#plot exec globals
count = 1000
start = 5
end = 400
step = 5

def plotExec(task):
    print(f'\nEpsilon: {task.epsilon}')
    print(f'Basepoint: {task.startpoint}\n')
    r = []
    for m in range(start,end+1,step):
        result = 0
        rnd.M = m
        for i in range(count):
            x,y,z = rnd.calculate(task)
            if z <= task.epsilon:
                result += 1
        print(f'Vector count (M): {m}; Result = {result}/{count}')
        r.append(result/count)
    return(r)

        
derivX = base.function(
        lambda x,y : 2*(200*x*(x*x-y)+x-1), #Func
        lambda x,y : 1200*x*x-400*y+2, #Deriv1
        lambda x,y : -400*x #Deriv2
        )
derivY = base.function(
        lambda x,y : -200*(x*x-y), #Func
        lambda x,y : -400*x, #Deriv1
        lambda x,y : 200  #Deriv2
        )
func   = base.function(
        lambda x,y : 100*(x*x-y)**2+(x-1)**2,
        derivX,
        derivY
        )

task = base.task(func, .001, startpoint = (-1., 1.))
#task.epsilon1d = .00000001

#task.epsilon = .1
#base.plotTask(task, 3)

task.epsilon = .001
task.epsilon1d = .000001
r1 = plotExec(task)

task.epsilon = .00001
task.epsilon1d = .00000001
r2 = plotExec(task)

#build hist
import plotly.express as px
fig = px.scatter({"x": list(range(start,end+1,step)), "e=0.001":r1, "e=0.00001":r2}, x="x", y=["e=0.001","e=0.00001"], labels={'x': 'Vector count (M)', "y": f'Success rate (out of {count})'}, title = f"Success rate (out of {count})")
fig.update_traces(marker_size = 10)
fig.show()

