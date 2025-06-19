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
waza = [LI() for _ in range(n)]

dp = [-1]*(n+1)
visited = [False]*(n+1)
def dfs(now):
  if visited[now]:
    return 0
  visited[now] = True
  t = waza[now-1][0]
  k = waza[now-1][1]
  A = waza[now-1][2:]
  
  tmp = 0
  for i in range(k):
    tmp += dfs(A[i])
  
  dp[now] = tmp+t
    
  return dp[now]

dfs(n)

print(dp[n])
