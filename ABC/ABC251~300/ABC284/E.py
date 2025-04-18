import sys
import collections, heapq, string, math, itertools, copy, bisect
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

n,m = MI()

connect = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = MI()
  connect[u].append(v)
  connect[v].append(u)
  
ans = 0

visited = [False]*(n+1)
def dfs(now):
  global ans
  ans += 1
  if ans >= 10**6:
    print(10**6)
    exit()
    
  visited[now] = True
  for to in connect[now]:
    if visited[to] == False:
      dfs(to)
  visited[now] = False
  
dfs(1)
print(ans)