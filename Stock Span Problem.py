# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 23:48:35 2021

@author: Saptarshi
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
    