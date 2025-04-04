import sys
import collections, heapq, string, math, itertools, copy
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

res = list(reversed(range(1,n)))

connect = [[] for _ in range(n+1)]
for _ in range(n-1):
  u,v = MI()
  connect[u].append(v)
  connect[v].append(u)
  

visited = [False]*(n+1)
lr = [[] for _ in range(n+1)]
def dfs(now):
  visited[now] = True
  l = n
  r = -1
  for to in connect[now]:
    if visited[to] == False:
      dfs(to)
      l = min(l,lr[to][0])
      r = max(r,lr[to][1])
 
  if l == n and r == -1:
    l = r = res.pop()
 
  lr[now] = [l,r]
  
dfs(1)
  
for i in range(1,n+1):
  print(*lr[i])