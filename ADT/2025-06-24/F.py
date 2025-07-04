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

n,x = MI()

dp = [[False]*(x+1) for _ in range(n+1)]

dp[0][0] = True
for i in range(n):
  a,b = MI()
  for j in range(x+1):
    if j+a <= x:
      dp[i+1][j+a] = dp[i+1][j+a] or dp[i][j]
    if j+b <= x:
      dp[i+1][j+b] = dp[i+1][j+b] or dp[i][j]

if dp[n][x]:
  print("Yes")
else:
  print("No")