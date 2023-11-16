import methods.decimal as decimal
import methods.vector as vec
from math import sqrt

vanilla = False
alternativeVectors = False
step = 4
gamma = 20

def calculate(task):
    global step

    func = task.func
    xk = task.startpoint
    e = task.epsilon
    e1d = task.epsilon1d

    sigma = 1/gamma

    if alternativeVectors:
        basevectors = [
            (1.,1.),
            (-1.,1.),
                ]
    else:
        basevectors = [
            (1.,0.),
            (0.,1.),
                ]

    for bv in basevectors:
        bv = vec.normalize(bv)

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
                break
            elif z2 < z:
                #print('z2')
                xk = vec.sub(xk, bv)
                zn = z2
                break
        else:
            #print('divide')
            step *= sigma
            #basevectors[i] = vec.mulC(bv,sigma)

        #Using alternative method
        #zn = func.get(*xk)
        if vanilla:
            #if abs(z-zn) < e and z != zn:
            if step < e and abs(z-zn) < e:
                return (*xk , zn)
        else: 
            if vec.vlen(func.grad(*xk)) < e:
                return (*xk , zn)
            elif step < e1d:
                print(f'[FAILSAFE | {__name__}] STEP is ZERO!')
                return (*xk , zn)
        z = zn
