#2D Matrix hell
# [[...], ...]

def size(m):
    return (len(m),len(m[0]))

def modulo(m):
    return sum([sum(i) for i in m])

def determ(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]

def invert(m):
    d = determ(m)

    at = [
        [m[1][1],-m[0][1]],
        [-m[1][0],m[0][0]]
            ]

    return mulC(at,1/d)

def sub(m1,m2):
    m = [[e for e in row] for row in m1] 

    row,col = size(m)

    for r in range(row):
        for c in range(col):
            m = m1[r][c] - m2[r][c]

    return m

def mulC(m,c):
    return [[e*c for e in row] for row in m] 

def add(m1,m2):
    m = [[e for e in row] for row in m1] 

    row,col = size(m)

    for r in range(row):
        for c in range(col):
            m = m1[r][c] + m2[r][c]

    return m

def mulM(m1,m2):
    #TODO
    return None
