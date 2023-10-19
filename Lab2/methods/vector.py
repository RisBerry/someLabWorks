#Vector operations
from math import sqrt

def size(v):
    return len(v)

def normalize(v):
    l = vlen(v)
    return [e/l for e in v]

def vlen(v):
    return sqrt(sum([e*e for e in v])) 

def sub(v1,v2):
    return [v1[i]-v2[i] for i in range(len(v1))]

def add(v1,v2):
    return [v1[i]+v2[i] for i in range(len(v1))]

def mulC(v,c):
    return [e*c for e in v] 

def mulV(v1,v2):
    return [v1[i]*v2[i] for i in range(len(v1))]
