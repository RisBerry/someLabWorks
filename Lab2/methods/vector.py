#Vector operations
from math import sqrt

def size(v):
    return len(v)

def normalize(v):
    l = vlen(v)
    return [e/l for e in v]

def sumarray(varray):
    return (sum([v[0] for v in varray]),sum([v[1] for v in varray]))

def vlen(v):
    return sqrt(sum([e*e for e in v])) 

def sub(v1,v2):
    return [v1[i]-v2[i] for i in range(len(v1))]

def add(v1,v2):
    return [v1[i]+v2[i] for i in range(len(v1))]

def addC(v, c):
    return [v[i]+c for i in range(len(v))]

def mulC(v,c):
    return [e*c for e in v] 

def mulV(v1,v2):
    return [v1[i]*v2[i] for i in range(len(v1))]
