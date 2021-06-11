# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 23:48:35 2021

@author: Saptarshi

Question - The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stock’s price for
all n days. 
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the
current day is less than or equal to its price on the given day.
"""

arr = list(map(int,input().split()))
n = len(arr)
stack = []
ans = []


for i in range(n):
    
    if len(stack)==0:
        ans.append(-1)
    elif len(stack)>0 and stack[-1][0] > arr[i]:
        ans.append(stack[-1][1])
    
    elif len(stack) > 0 and stack[-1][0] <=arr[i]:
        while len(stack) > 0 and stack[-1][0] <=arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1][1])
    
    stack.append([arr[i] , i])

for i in range(len(ans)):
    ans[i] = i - ans[i]

print(ans)

#O(n) representation by Stack.
    
