import sys
import collections, heapq, string, math, itertools

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
c = LS()
c.insert(0,'')
connect = [[] for _ in range(n+1)]
for _ in range(n-1):
  a,b = MI()
  connect[a].append(b)
  connect[b].append(a)

dp = [[0]*3 for _ in range(n+1)]

visited = [False]*(n+1)
visited[1] = True

def dfs(now, visited, dp):
  tmp1 = 1
  tmp2 = 1
  for to in connect[now]:
    if visited[to] == False:
      visited[now] = True
      dfs(to,visited,dp)
      if c[now] == 'a':
        tmp1 *= (dp[to][0] + dp[to][2])%mod
      else:
        tmp1 *= (dp[to][1] + dp[to][2])%mod
      tmp2 *= (dp[to][0] + dp[to][1] + 2*dp[to][2])%mod
    
  if c[now] == 'a':
    dp[now][0] = tmp1%mod
  else:
    dp[now][1] = tmp1%mod
  dp[now][2] = (tmp2-tmp1)%mod

dfs(1,visited,dp)

print(dp[1][2]%mod) 