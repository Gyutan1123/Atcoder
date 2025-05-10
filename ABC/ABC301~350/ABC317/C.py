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
n,m = MI()

graph = [[-1]*(n+1) for _ in range(n+1)]
for _ in range(m):
  u,v,c = MI()
  graph[u][v] = c
  graph[v][u] = c
  
ans = 0
for p in itertools.permutations(range(1,n+1)):
  now = p[0]
  
  tmp = 0
  flag = True
  for i in range(n-1):
    if graph[now][p[i+1]] == -1:

      break
    else:
      tmp += graph[now][p[i+1]]
      now = p[i+1]
  
  ans = max(ans,tmp)

print(ans)