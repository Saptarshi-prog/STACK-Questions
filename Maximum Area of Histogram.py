# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:49:23 2021

@author:Saptarshi
"""

def NSL_index(arr,n):
    pseudo_index = -1
    stack = []
    left = []
    i=0
    for i in range(n):
        if len(stack) == 0:
            left.append(pseudo_index)
        elif len(stack)>0 and stack[-1][0]<arr[i]:
            left.append(stack[-1][1])
        
        elif len(stack)>0 and stack[-1][0] >=arr[i]:
            while len(stack)>0 and stack[-1][0] >=arr[i]:
                stack.pop()
            if len(stack)==0:
                left.append(pseudo_index)
            else:
                left.append(stack[-1][1])
        stack.append([arr[i], i])
    return left


def NSR_index(arr,n):
    pseudo_index = n
    stack = []
    right = []
    i=0
    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            right.append(pseudo_index)
        elif len(stack)>0 and stack[-1][0]<arr[i]:
            right.append(stack[-1][1])
        elif len(stack)>0 and stack[-1][0] >=arr[i]:
            while len(stack)>0 and stack[-1][0] >=arr[i]:
                stack.pop()
            if len(stack)==0:
                right.append(pseudo_index)
            else:
                right.append(stack[-1][1])
        stack.append([arr[i],i])
    right.reverse()
    return right

arr = list(map(int,input().split()))
n = len(arr)

width = []
area = []
right_index = NSR_index(arr,n)
left_index = NSL_index(arr,n)

for i in range(n):
    width.append((right_index[i]-left_index[i])-1)
for i in range(n):
    area.append(width[i]*arr[i])
ans = max(area)
print(ans)
