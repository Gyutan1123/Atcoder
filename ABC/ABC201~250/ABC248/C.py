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
mod = 998244353
########################################################

n,m,k = MI()

dp = [[0]*(k+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(n):
  for j in range(k+1):
    for l in range(1,m+1):
      if j+l <= k:
        dp[i+1][j+l] += dp[i][j]%mod
        
print(sum(dp[n])%mod)