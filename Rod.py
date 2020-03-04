# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:39:32 2020

@author: Simon
"""
i1 = 0
def cut_rod_rec(prices, n):
    global i1
    i1 += 1
    if n <= 0:
        return 0
    max_val = prices[n]
    for i in range(1,n):        
        max_val = max(max_val, prices[i] + cut_rod_rec(prices, n-i))
    return max_val

prices = [0,1,5,8,9,10,17,17,20,24,30]



values = [0]*(len(prices))
cuts = [0]*(len(prices))
count = 0
def cut_rod(prices,n):
    global values 
    global cuts
    global count
    count += 1
    cut = n
    max_val = -1
    
    for i in range(1, n+1):
        if (values[n-i] == -1):
            values[n-i] = cut_rod(prices, n-i)
        if (max_val < prices[i] + values[n-i]):
            max_val = prices[i] + values[n-i]
            cut = i
            
    cuts[n] = cut
    values[n] = max_val
    return max_val

for i in range(1, len(values)):
    values[i] =-1

print(cut_rod(prices,8))
print(count)

print(cuts)
def cut_rod_it(prices,n):
    max_val = prices[n]
    
    for i in range(1,n//2+1):
        max_val = max(max_val, prices[i] + prices[n-i])
    return max_val









    

