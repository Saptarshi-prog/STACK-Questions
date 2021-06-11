# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 22:48:31 2021

@author: Saptarshi

In a given array find the nearest greater element of every element in the array to the right of it. If none is greater return -1.
"""
arr = list(map(int,input().split()))
n = len(arr)
stack = []
ans = []

for i in range(n-1,-1,-1):      #traversing in revresed manner i.e traversing from right towards left
    if len(stack)==0:
        ans.append(-1)
    elif len(stack)>0 and stack[-1]>arr[i]:
        ans.append(stack[-1])
    elif len(stack)>0 and stack[-1]<=arr[i]:
        while len(stack)>0 and stack[-1]<=arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
    stack.append(arr[i])
    
ans.reverse()
print(ans)
