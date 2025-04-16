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
mod = 10**9 + 7
########################################################

n,k,d = MI()
a = LI()

dp = [[[-1]*d for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
  dp[i][0][0] = 0

for i in range(n):
  for j in range(1,k+1):
    if j > i+1:
      continue
    for l in range(d):
      dp[i+1][j][l] = dp[i][j][l]
    for l in range(d):
      if dp[i][j-1][l] != -1:
        dp[i+1][j][(l+a[i])%d] = max(dp[i+1][j][(l+a[i])%d], a[i]+dp[i][j-1][l])

print(dp[n][k][0])
