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

n,m,k = MI()

inv = pow(m,-1,mod)

dp = [[0]*(n+1) for _ in range(k+1)]

dp[0][0] = 1
for i in range(k):
  dp[i+1][n] += dp[i][n]%mod
  for j in range(n):
    
    for l in range(1,m+1):
      if j+l <= n:
        dp[i+1][j+l] += (dp[i][j]*inv)%mod
        dp[i+1][j+l] %= mod
      else:
        d = (j+l)-n
        dp[i+1][max(0,n-d)] += (dp[i][j]*inv)%mod
        dp[i+1][max(0,n-d)] %= mod


print(dp[k][n]%mod)