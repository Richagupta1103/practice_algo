from time import time
'''
Top down approach
'''

def wayOfClimb(n):
        if n<0:
            return 0
        elif n==0:
            return 1
        else:
            memo = [0]*(n+1)
            memo[1] = 1
            memo[2] = 2
            memo[3] = 4
            for i in range(4,n+1):
                memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
            print memo[n]

class DynamicProblem():
    s = time()
    n=1000
    wayOfClimb(n)
    e = time()
    print e-s