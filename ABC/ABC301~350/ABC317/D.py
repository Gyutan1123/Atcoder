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

xyz = [LI() for _ in range(n)]
sz = sum([xyz[i][2] for i in range(n)])

dp = [[float('inf')] * (sz+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
  for j in range(sz+1):
    x,y,z = xyz[i]
    dp[i+1][j] = min(dp[i+1][j],dp[i][j])
    if x > y and j >= z:
      dp[i+1][j] = min(dp[i+1][j], dp[i][j-z])
    if x < y and j >= z:
      dp[i+1][j] = min(dp[i+1][j], dp[i][j-z]+(y-x+1)//2)

ans = float('inf')  
for z in range(sz//2+1, sz+1):
  ans = min(ans, dp[n][z])
print(ans)