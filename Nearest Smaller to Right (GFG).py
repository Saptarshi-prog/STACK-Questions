# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 00:09:55 2021

@author: Saptarshi
"""
arr = list(map(int,input().split()))
n = len(arr)
stack = []
ans = []

for i in range(n-1,-1,-1):
    if len(stack)==0:
        ans.append(-1)
    elif len(stack)>0 and stack[-1]<arr[i]:
        ans.append(stack[-1])
    elif len(stack)>0 and stack[-1]>=arr[i]:
        while len(stack)>0 and stack[-1]>=arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
    stack.append(arr[i])
    
ans.reverse()
print(ans)