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

n,x,y = MI()
connect = [[] for _ in range(n+1)]
for _ in range(n-1):
  u,v = MI()
  connect[u].append(v)
  connect[v].append(u)
  
visited = [False]*(n+1)
pre = [-1]*(n+1)
def dfs(now):
  visited[now] = True
  for to in connect[now]:
    if visited[to] == False:
      visited[to] = True
      pre[to] = now
      
      global y
      if to == y:
        return
      
      dfs(to)
    
dfs(x)
ans = []
now = y
while pre[now] != -1:
  ans.append(now)
  now = pre[now]
ans.append(x)  

ans.reverse()

print(*ans)