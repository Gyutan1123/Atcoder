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
mod = 998244353
########################################################

S = SI()
n = len(S)
dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
  for j in range(n):
    s = S[i]
    if s == '(' and j+1 <= n:
      dp[i+1][j+1] += dp[i][j]%mod
    if s == ')' and j-1 >= 0:
      dp[i+1][j-1] += dp[i][j]%mod
    
    if s == '?':
      if j+1 <= n:
        dp[i+1][j+1] += dp[i][j]%mod
      if j-1 >= 0:
        dp[i+1][j-1] += dp[i][j]%mod
     
print(dp[n][0]%mod)
