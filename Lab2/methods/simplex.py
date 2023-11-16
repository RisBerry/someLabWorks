import methods.decimal as decimal
import methods.matrix as matrix
import methods.vector as vec
from math import sqrt

vanilla = True
allPoints = False
useGrad = True
allowTriangleFlip = False
l = 10
sigma = 0.5
alwaysDump = False

def findMin(s):
    p1 = s[0][-1]
    p2 = s[1][-1]
    p3 = s[2][-1]
    if p1[2] < p2[2] and p1[2] < p3[2]:
        return 0
    elif p2[2] < p1[2] and p2[2] < p3[2]:
        return 1
    else:
        return 2

def sortByMax(s):
    p1 = [*s[0][-1],0]
    p2 = [*s[1][-1],1]
    p3 = [*s[2][-1],2]
    return [p[3] for p in sorted([p1,p2,p3],key=lambda x: x[2])]

def midPoint(s):
    array = []
    for p in s:
        array.append(p[-1][0:2])
    #print(vec.mulC(vec.sumarray(array),1/3)[0:2])
    return vec.mulC(vec.sumarray(array),1/3)[0:2]

def calculate(task):
    func = task.func
    xk = task.startpoint
    e = task.epsilon
    e1d = task.epsilon1d

    #build simplex cords
    n = 2
    t1 = l*(sqrt(n+1)-1)/(n*sqrt(2))
    t2 = l*(sqrt(n+1)+n-1)/(n*sqrt(2))
    ll = l
    simplex = [
            [[*xk,None]],
            [[xk[0]+t1,xk[1]+t2,None]],
            [[xk[0]+t2,xk[1]+t1,None]],
            ]
    #print(simplex)

    #Calculate
    for s in simplex:
        s[0][2] = func.get(s[0][0],s[0][1])


    lastMirror = None

    itter = 0

    while True:
        if vanilla:
            xyz = simplex[findMin(simplex)][-1]
        else:
            xy = midPoint(simplex)
            xyz = [*xy, func.get(*xy)]

        if useGrad:
            grad = func.grad(*xyz[0:2])
            if vec.vlen(grad) < e:
                if alwaysDump:
                    simplexDump(simplex)
                return (xyz)
            elif ll == 0.0:
                print(f'[FAILSAFE | {__name__}] Triangle length is ZERO!')
                #print(f'[FAILSAFE | {__name__}] {ll:.16f} {midPoint(simplex)} {grad}')
                if alwaysDump:
                    simplexDump(simplex)
                return (xyz)
        else:
            if ll < e:
                if alwaysDump:
                    simplexDump(simplex)
                return (xyz)

        mX = sortByMax(simplex)
        if lastMirror is not None:
            mX.remove(lastMirror)

        #calculate mirror point or divide

        mp = midPoint(simplex)
        bestCase = None
        for i in mX:
            i = mX[-1]
            mirror = simplex[i][-1]
            point = mirror[0:2]
            v = vec.add(vec.mulC(vec.sub(mp,point),3),point)
            z = func.get(*v)
            if z < mirror[2]:
                if not allPoints:
                    lastMirror = i
                    simplex[i].append([*v,z])
                    #print(f'MIROR!(first){i}')
                    break
                else:
                    bestCase = (i,v,z)
        else:
            if bestCase is not None and allPoints:
                i,v,z = bestCase
                lastMirror = i
                simplex[i].append([*v,z])
                #print(f'MIROR!(all){i}')
            else:
                flipSuccsess = False
                if allowTriangleFlip and lastMirror is not None:

                    p1 = simplex[mX[0]][-1][0:2]
                    p2 = simplex[mX[1]][-1][0:2]

                    flip = simplex[lastMirror][-1]
                    flipPoint = flip[0:2]
                    flipVec = vec.mulC(vec.sub(mp,flipPoint),-3)
                    checkPoint = vec.add(vec.mulC(flipVec,0.5),flipPoint)
                    z = func.get(*checkPoint)
                    if z < flip[2]:
                        #print('FLIP!')
                        flipSuccsess = True
                        for i in mX:
                            p = vec.add(simplex[i][-1][0:2],flipVec)
                            simplex[i].append([*p,func.get(*p)])

                if not flipSuccsess:
                    #Subdivide
                    ll*=sigma
                    lastMirror = None
                    m = findMin(simplex) if lastMirror is None else lastMirror
                    #print(f'SUBDI!{m}')
                    p = [0,1,2]
                    p.remove(m)
                    basePoint = simplex[m][-1]
                    for j in p:
                        subd = vec.add(vec.mulC(vec.sub(simplex[j][-1],basePoint),sigma),basePoint)
                        subd[2] = func.get(*subd[0:2])
                        simplex[j].append(subd)

        itter += 1

        if itter > 100000:
        #if itter > 10:
            grad = func.grad(*xyz[0:2])
            print(f'[FAILSAFE | {__name__}] {ll:.16f} {midPoint(simplex)} {grad}')
            simplexDump(simplex)
            return None

def simplexDump(simplex):
    from plotly.offline import plot
    import plotly
    from plotly.graph_objs import Scatter,Figure
    fig = Figure()
    output = [Scatter(x = [p[0] for p in s], y = [p[1] for p in s]) for s in simplex]
    fig.add_traces(output)
    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )
    fig.show()
    #plot(fig,filename = 'failsafe.html',show_link=False)
