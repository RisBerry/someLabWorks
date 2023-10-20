import methods.decimal as decimal
import methods.matrix as matrix
import methods.vector as vec
from math import sqrt

l = 2
sigma = 0.25

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

def calculate(task):

    func = task.func
    xk = task.startpoint
    e = task.epsilon
    e1d = task.epsilon1d

    #build simplex cords
    n = 2
    t1 = l*(sqrt(n+1)-1)/(n*sqrt(2))
    t2 = l*(sqrt(n+1)+n-1)/(n*sqrt(2))
    simplex = [
            [[*xk,None]],
            [[xk[0]+t1,xk[0]+t2,None]],
            [[xk[0]+t2,xk[0]+t1,None]],
            ]

    #Calculate
    for s in simplex:
        s[0][2] = func.get(s[0][0],s[0][1])


    lastMirror = None

    while True:
        xyz = simplex[findMin(simplex)][-1]
        grad = func.grad(*xyz[0:2])
        if vec.vlen(grad) < e:
            return (xyz)

        mX = sortByMax(simplex)
        if lastMirror is not None:
            mX.remove(lastMirror)

        #calculate mirror point
        #TODO: Try all possible mirrors

        i = mX[-1]
        mirror = simplex[i][-1]
        array = []
        for p in simplex:
            array.append(p[-1][0:2])
        v = vec.mulC(vec.sub(vec.mulC(vec.sumarray(array),1/3),mirror[0:2]),3)
        z = func.get(*v)
        if z < mirror[2]:
            lastMirror = i
            simplex[i].append([*v,z])
        else:
            lastMirror = None
            m = findMin(simplex)
            p = [0,1,2]
            p.remove(m)
            basePoint = simplex[m][-1]
            for j in p:
                subd = vec.add(vec.mulC(vec.sub(simplex[j][-1],basePoint),sigma),basePoint)
                subd[2] = func.get(*subd[0:2])
                simplex[j].append(subd)
