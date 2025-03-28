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

n = II()

connect = [[] for _ in range(n+1)]
for _ in range(n-1):
  u,v = MI()
  connect[u].append(v)
  connect[v].append(u)

dp = [0]*(n+1)
ans = [0]*(n+1)
visited = [False]*(n+1)
dist = [0]*(n+1)
def dfs(now, visited, dp, dist, nowDist):
  visited[now] = True
  dist[now] = nowDist
  ans[1] += nowDist
  dp[now] += 1
  for to in connect[now]:
    if visited[to] == False:
      dfs(to, visited, dp, dist, nowDist+1)
      dp[now] += dp[to]
      
dfs(1,visited,dp,dist,0)

que = collections.deque()
que.append(1)
visited = [False]*(n+1)
visited[1] = True
while que:
  now = que.popleft()
  for to in connect[now]:
    if visited[to] == False:
      visited[to] = True
      que.append(to)
      ans[to] = ans[now]+n-2*dp[to]
      
for i in range(1,n+1):
  print(ans[i])