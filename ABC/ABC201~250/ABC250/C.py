import sys
import collections, heapq, string, math, itertools, copy, bisect
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

n,q = MI()
A = [i for i in range(1,n+1)]

d = dict()
for i in range(n):
  d[i+1] = i

for _ in range(q):
  x = II()
  
  i = d[x]
  
  if i == n-1:
    d[A[n-2]] = n-1
    d[A[n-1]] = n-2
    A[n-2],A[n-1] = A[n-1],A[n-2]
    
  else:
    d[A[i]] = i+1
    d[A[i+1]] = i
    A[i],A[i+1] = A[i+1],A[i]
    
print(*A)