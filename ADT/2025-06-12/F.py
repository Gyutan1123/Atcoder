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

dp = [[0]*(k+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(1,n+1):
  for j in range(1,m+1):
    for l in range(k+1):
      if l+j > k:
        break
      dp[i][l+j] += (dp[i-1][l])%mod
      
    
ans = 0
for i in range(k+1):
  ans += dp[n][i]
  ans %= mod
print(ans)