# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 08:37:40 2020

@author: Simon
"""

i = 0

def fib(n):
    global i
    i += 1
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)



i2 = 0
values = []
def fib_dyn(n):
    global values
    global i2
    i2 += 1
    if len(values) == 0:
        values = [0]*(n+1)
        values[1] = 1
        values[2] = 1
    if values[n] != 0:
        return values[n]
    values[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return values[n]


i3 = 0
def fib_it(n):
    a = 0 
    b = 1
    global i3
    for i in range(1, n):
        i3 += 1
        c = a
        a = b
        b = a + c
    return b

print(fib_it(40))
print(i3)
print(fib_dyn(40))
print(i2)    





