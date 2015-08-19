'''
Created on Aug 18, 2015

@author: Ruu
'''

n = int(input())
case = 1
while n != 0:
    solution = pow(n, n - 2)
    print("Case %d, N = %d, # of different labelings = %d" % (case, n, solution))
    case += 1
    n = int(input())