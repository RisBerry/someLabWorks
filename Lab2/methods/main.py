#2D Matrix hell
# [[...], ...]

def size(m):
    return (len(m),len(m[0]))

def modulo(m):
    #TODO
    return None

def sub(m1,m2):
    m = [[e for e in row] for row in m1] 

    row,col = size(m)

    for r in range(row):
        for c in range(col):
            m = m1[r][c] - m2[r][c]

    return m

def mulC(m,c):
    return [[e*C for e in row] for row in m1] 

def add(m1,m2):
    m = [[e for e in row] for row in m1] 

    row,col = size(m)

    for r in range(row):
        for c in range(col):
            m = m1[r][c] + m2[r][c]

    return m

def mulM(m1,m2):
    return None
