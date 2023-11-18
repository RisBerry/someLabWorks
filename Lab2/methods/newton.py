import methods.decimal as decimal
import methods.matrix as matrix
import methods.vector as vec
from methods.base import frange
from math import sqrt
from math import isnan

from random import random

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
from plotly.graph_objs import *

jitter = False
multiply = .1
maxTrys = 5

decimalSearch = False
decimalLength = 1.

alwaysDump = False

def eCmp(a,b,e):
    return abs(a-b) <= e

def calculate(task):
    func = task.func
    xk = task.startpoint
    e = task.epsilon
    e1d = task.epsilon1d

    dumps = []

    trys = 0
    oldxk = None
    if not jitter:
        trys = maxTrys

    while True:
        if alwaysDump:
            dumps.append(xk)

        #print(xk,oldxk,trys)
        if isnan(xk[0]):
            print(f'[ASSERT | {__name__}] NaN detected')
            return None

        grad = func.grad(*xk)
        if vec.vlen(grad) < e and trys == maxTrys:
            if alwaysDump:
                plotNewton(func,xk,0.1,5,dumps)
            z = func.get(*xk)
            return (*xk , z)
        elif jitter and oldxk is not None:
            if eCmp(xk[0],oldxk[0],e) and eCmp(xk[1],oldxk[1],e):
                trys += 1

                jtr = vec.normalize((random()*2-1.,random()*2-1.)) #Direction
                jtr = vec.mulC(jtr,multiply*trys)

                oldxk = xk[:]
                xk = vec.add(xk,jtr)

            else:
                trys = 0



        hess = matrix.invert(func.hess(*xk))

        if hess is None:
            print(f'[ASSERT | {__name__}] Determinat is zero')
            return None

        #grad = func.grad(*xk)

        tmpX = hess[0][0]*grad[0] + hess[0][1]*grad[1]
        tmpY = hess[1][1]*grad[1] + hess[1][0]*grad[0]
        tmp = (tmpX,tmpY)

        #print(xk,grad,tmp)
        if trys == 0:
            oldxk = xk[:]

        if decimalSearch:
            a = decimalLength
            func1d = lambda ak: func.get(*vec.sub(xk, vec.mulC(c = ak, v = tmp) ))
            a = decimal.calculate(func1d, -a, a, e1d)
            tmp = vec.mulC(tmp,a)

        xk = vec.sub(xk,tmp)

def plotNewton(func, start, e, rad, dump, name = 'newton.html'):
    x,y = start
    xVar = frange(x-rad,x+rad,e)
    yVar = frange(y-rad,y+rad,e)
    zVar = [[func.get(x,y) for x in xVar] for y in yVar]
    xD = [d[0] for d in dump]
    yD = [d[1] for d in dump]
    output = [
            Contour(x = xVar, y = yVar, z = zVar, name = 'Our function', contours_coloring='lines', line_width=2,contours=dict( start=0, end=2000, size=40) ),
            Scatter (x = xD, y = yD)]
    plot(output,filename = name,show_link=False)

