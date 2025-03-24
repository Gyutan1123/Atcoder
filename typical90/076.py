import sys
import collections, heapq, string, math, itertools

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n = II()

A = LI()
wholeSize = sum(A)
if wholeSize % 10 != 0:
  print('No')
  exit()
A += A

tmp = 0
right = 0
ans = 'No'
for left in range(2*n):
  while (right < 2*n and tmp+A[right] <= wholeSize//10):
    tmp += A[right]
    right += 1
  if tmp == wholeSize//10 and right-left <= n:
    ans = 'Yes'
  
  if right == left:
    right += 1
  else:
    tmp -= A[left]
    
print(ans)