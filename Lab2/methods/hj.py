import methods.decimal as decimal
import methods.vector as vec
from math import sqrt

vanilla = False
step = 4
gamma = 20

def calculate(task):

    func = task.func
    xk = task.startpoint
    e = task.epsilon
    e1d = task.epsilon1d

    sigma = 1/gamma

    basevectors = [
        (1.,0.),
        (0.,1.),
            ]

    #basevectors = [
    #    (1.,1.),
    #    (-1.,1.),
    #        ]

    #for bv in basevectors:
    #    bv = vec.normalize(bv)

    z = func.get(*xk)
    zn = z

    failsafe = 0

    while True:
        #failsafe += 1

        #if failsafe == 10:
        #    print('failsafe')
        #    failsafe = 0
        #    basevectors = [vec.mulC(bv,sigma) for bv in basevectors]
        #    continue
        for i in range(len(basevectors)):
            bv = vec.mulC(basevectors[i],step)
            z1 = func.get(*vec.add(xk,bv))
            z2 = func.get(*vec.sub(xk,bv))

            if z1 < z:
                #print('z1')
                xk = vec.add(xk, bv)
                zn = z1
            elif z2 < z:
                #print('z2')
                xk = vec.sub(xk, bv)
                zn = z2
            else:
                #print('divide')
                basevectors[i] = vec.mulC(bv,sigma)

        #Using alternative method
        #zn = func.get(*xk)
        if vanilla:
            if abs(z-zn) < e and z != zn:
                return (*xk , zn)
        else: 
            if vec.vlen(func.grad(*xk)) < e:
                return (*xk , zn)

        z = zn
