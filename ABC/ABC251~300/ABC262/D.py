import sys
import collections, heapq, string, math, itertools, copy, bisect
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

n = II()
a = LI()

ans = n

for m in range(2,n+1):
  dp = [[[0]*m for _ in range(n+1)] for _ in range(n+1)]
  dp[0][0][0] = 1
  
  for i in range(n):
    for j in range(n):
      for k in range(m):
        dp[i+1][j][k] += dp[i][j][k]%mod
        dp[i+1][j+1][(k+a[i])%m] += dp[i][j][k]%mod
  
  ans += dp[n][m][0]%mod
  
print(ans%mod)