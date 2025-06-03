import sys
import collections, heapq, string, math, itertools, copy, bisect, functools
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

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
connect = [[] for _ in range(n+1)]
for i in range(n-1):
  u,v = MI()
  connect[u].append(v)
  connect[v].append(u)
  
count = [0]*(n+1)
visited = [False]*(n+1)
def dfs(v):
  visited[v] = True
  count[v] = 1
  if len(connect[v]) == 1:
    count[v] = 1
    return count[v]
  
  for to in connect[v]:
    if not visited[to]:
      count[v] += dfs(to)

  return count[v]

dfs(1)

ans = float('inf')
need = []
for to in connect[1]:
  need.append(count[to])
need.sort()
print(sum(need[:-1])+1)