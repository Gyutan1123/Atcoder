import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

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
dx = collections.defaultdict(lambda : 0)
dy = collections.defaultdict(lambda : 0)

p = [tuple(MI()) for _ in range(n)]

pset = set(p)

for i in range(n):
  for j in range(i+1,n):
    xi,yi = p[i]
    xj,yj = p[j]
    
    if xi == xj:
      dy[(max(yi,yj),min(yi,yj))] += 1
    if yi == yj:
      dx[(max(xi,xj),min(xi,xj))] += 1

ans = 0

for i in range(n):
  for j in range(i+1,n):
    xi,yi = p[i]
    xj,yj = p[j]
    
    if xi == xj:
      ans += dy[(max(yi,yj),min(yi,yj))] - 1
    elif yi == yj:
      ans += dx[(max(xi,xj),min(xi,xj))] - 1
    elif (xi,yj) in pset and (xj,yi) in pset:
      ans += 1
      
print(ans//6)