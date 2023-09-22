from methods.base import frange

def calculate(task):
    minX = task.xRange[0]
    maxX = task.xRange[1]
    epsilon = task.epsilon

    function = task.function
    
    answer = function(minX)
    
    for x in frange(minX+epsilon,maxX+epsilon,epsilon):
        if function(x) < answer:
            answer = function(x)
            minX = x


    return (minX,answer)
