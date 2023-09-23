from methods.base import frange

def calculate(task):
    minX = task.xRange[0]
    maxX = task.xRange[1]
    epsilon = task.epsilon

    function = task.function
    
    answer = function(minX)
    x = minX
    #minX+=epsilon
    
    itter = 1

    #print(minX,maxX,minX+epsilon,maxX+epsilon,len(frange(minX+epsilon,maxX+epsilon,epsilon)))
    #for x in frange(minX+epsilon,maxX+epsilon,epsilon):
    #    if function(x) < answer:
    #        answer = function(x)
    #        minX = x
    #    itter+=1
    #while minX<=maxX:
    #    if function(minX) < answer:
    #        answer = function(minX)
    #    print(minX)
    #    minX+=epsilon
    #    itter+=1

    #print((maxX-minX)/epsilon)
    for i in range(int((maxX-minX)/epsilon)):
        if function(minX+epsilon*(i+1)) < answer:
            answer = function(epsilon*(i+1)+minX)
            x=epsilon*(i+1)+minX
        #print(minX+epsilon*(i+1))
        #minX+=epsilon
        itter+=1

    return (x,answer,itter)
