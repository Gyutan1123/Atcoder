import sys
import collections, heapq, string, math, itertools, copy, bisect, functools
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

n = II()
A = LI()

d = [[0]*2 for _ in range(n+1)]
for i in range(1,n):
  d[A[i]][1] += 1
  

S = [0]*(n+1)

ans = 0
for i in range(n-1):
  if A[i] == A[i+1]:
    S[i+1] = S[i]-d[A[i]][0]*d[A[i]][1]
    S[i+1] += (d[A[i]][0]+1)*(d[A[i]][1]-1)
    d[A[i]][0] += 1
    d[A[i]][1] -= 1
  else:
    S[i+1] = S[i]-d[A[i]][0]*d[A[i]][1]
    S[i+1] -= d[A[i+1]][0]*d[A[i+1]][1]
    
    S[i+1] += (d[A[i]][0]+1)*d[A[i]][1]
    S[i+1] += d[A[i+1]][0]*(d[A[i+1]][1]-1)
    
    d[A[i]][0] += 1
    d[A[i+1]][1] -= 1
  
  ans += S[i+1] - d[A[i+1]][0]*d[A[i+1]][1]
  

print(ans)
  