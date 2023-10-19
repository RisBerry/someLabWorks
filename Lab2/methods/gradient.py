import methods.decimal as decimal
import methods.vector as vec

restart = 1*2+1

def calculate(task):

    func = task.func
    xk = task.startpoint
    e = task.epsilon

    k = 0
    n = restart

    grad = None
    p0 = None
    p0n = None

    while True:
        if k == 0:
            #Step 1
            grad = func.grad(*xk)
            if vec.vlen(grad) < e:
                return (*xk , func.get(*xk))
            
            #Step 2
            #k = 0

            #Crutch
            #Lets use normalized vector for p0
            p0 = vec.mulC(grad, -1.)
            p0n = vec.normalize(p0)
        else:
            #Skip step 1 and 2
            pass

        #Step 3
        #a = max(e, vec.vlen(grad))
        a = vec.vlen(grad)
        #print(k,p0,xk,a)
        func1d = lambda ak: func.get(*vec.add(xk, vec.mulC(c = ak, v = p0n) ))


        #print('[s1]',xk,p0n,a)
        a = decimal.calculate(func1d, e, a, e)

        #Step 4
        xkn = vec.add(xk, vec.mulC(c = a, v = p0n))

        gradn = func.grad(*xkn)
        if vec.vlen(gradn) < e:
            return (*xkn , func.get(*xkn))
    
        #Step 5
        k += 1
        if k == n:
            xk = xkn
            #print(f'[WARN|{__name__}] Gradient itteration reset!')
            k = 0
            #return None
            continue

        #step 6
        b = vec.vlen(gradn)**2 / vec.vlen(grad)**2
        p1 = vec.sub(vec.mulC(p0,b),gradn)
        p0 = p1
        p0n = vec.normalize(p1)

        #Crutch
        #Lets calculate p1 using only normalized vectors
        #p1 = vec.sub(p0n, vec.normalize(gradn))
        #p0n = p1

        #Next itteration
        grad = gradn
        xk = xkn
