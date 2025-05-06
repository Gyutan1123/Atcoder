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
mg = II()
graphg = [[False]*(n+1) for _ in range(n+1)]
for _ in range(mg):
  u,v = MI()
  graphg[u][v] = True
  graphg[v][u] = True
  
mh = II()
graphh = [[False]*(n+1) for _ in range(n+1)]
for _ in range(mh):
  u,v = MI()
  graphh[u][v] = True
  graphh[v][u] = True
  
A = [LI() for _ in range(n-1)]

ans = float('inf')
for p in itertools.permutations(range(1,n+1)):
  tmp = 0
  for i in range(1,n+1):
    for j in range(i+1,n+1):
      if graphg[i][j] != graphh[p[i-1]][p[j-1]]:
        ih,jh = min(p[i-1],p[j-1]),max(p[i-1],p[j-1])
        tmp += A[ih-1][jh-ih-1]
  ans = min(ans,tmp)
print(ans)