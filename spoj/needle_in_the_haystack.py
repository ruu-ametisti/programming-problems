'''
Created on Aug 8, 2015

@author: Ruu
'''

def find_needles(needle_length, needle, haystack):
    i = 0
    lst = []
    while i < len(haystack):
        if haystack[i] == needle[0] and needle == haystack[i:i + needle_length]:
            lst.append(i)
            i += 1
        else:
            i += 1
            
    return lst

while True:
    try:
        needle_length = int(input())
        needle = input()
        haystack = input()
    except EOFError:
        break
    
    if needle_length > len(haystack):
        continue
    
    lst = find_needles(needle_length, needle, haystack)
    i = 0
    while i < len(lst):
        print(lst[i])
        i += 1
    print("")