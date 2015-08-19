'''
Created on Aug 8, 2015

@author: Ruu
'''

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
lines = int(input())
i = 0

while i < lines:
    n = input()
    print(factorial(int(n)))
    i += 1