import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

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
A = LI()

dp = [[0]*10 for _ in range(n)]
dp[0][A[0]] = 1

for i in range(n-1):
  for j in range(10):
    f = (j+A[i+1])%10
    g = (j*A[i+1])%10
    dp[i+1][f] += dp[i][j] % mod
    dp[i+1][g] += dp[i][j] % mod
    
for k in range(10):
  print(dp[n-1][k]%mod)