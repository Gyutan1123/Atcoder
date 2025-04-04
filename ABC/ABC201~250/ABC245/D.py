import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n,m = MI()
A = LI()
C = LI()

A += [0]*m
B = [0]*(n+m+1)

for l in range(n+1):
  if A[l] != 0:
    break


for j in range(m+1):
  s = 0
  for i in range(j):
    s += B[i]*A[j+l-i]
    
  B[j] = (C[j+l]-s)//A[l]
  
print(*B[:m+1])