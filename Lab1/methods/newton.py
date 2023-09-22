from methods.base import frange

def calculate(task):
    a = task.xRange[0]
    b = task.xRange[1]
    epsilon = task.epsilon

    function = task.function
    diff1 = task.diff1
    diff2 = task.diff2


    if diff1 is None or diff2 is None:
        print(f'[ASSERT|{__name__}] Some diff function is not available')
        return None

    x0 = a

    failsafe = 0

    #while a <= x0 <= b:
    while True:
        x1 = x0 - diff1(x0)/diff2(x0)

        if x1 < a or x1 > b:
            failsafe += 1
        if failsafe >= 10:
            print(f'[ASSERT|{__name__}] Newton method failed (failsafe out of range limit {x1:.4f})')
            return None

        x1 = min(max(x1,a),b) # Limit Newton's method to our limits.
        if abs(x1 - x0) <= epsilon:
            return x1, function(x1)
        x0 = x1

    #print(f'[ASSERT|{__name__}] Newton method failed (???)')
