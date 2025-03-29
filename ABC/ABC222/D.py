import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

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
b = LI()
dp = [[0]*(3001) for _ in range(n+1)]
dp[0][0] = 1
accum = [1]*(3002)
accum[0] = 0

for i in range(n):
  for j in range(3001):
    if a[i] <= j and j <= b[i]:
      dp[i+1][j] += accum[j+1] % mod
   
  accum = [0]*(3002)
  for j in range(3001):
    accum[j+1] = accum[j]+dp[i+1][j]

print(sum(dp[n])%mod)