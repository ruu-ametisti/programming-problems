'''
Created on Aug 8, 2015

@author: Ruu
'''

def reverse_string(s):
    i = len(s) - 1
    s2 = ""
    while i >= 0:
        s2 += s[i]
        i -= 1
    return s2

def remove_zeros(s):
    if s[0] == "0":
        return remove_zeros(s[1:])
    else:
        return s

lines = int(input())
i = 0

while i < lines:
    line = input()
    (str1, str2) = line.split(" ", 1)
    num1 = int(reverse_string(str1))
    num2 = int(reverse_string(str2))
    sum = num1 + num2
    
    sumstr = reverse_string(str(sum))
    result = remove_zeros(sumstr)
    
    print(result)
    i += 1