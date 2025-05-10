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
D = [LI() for _ in range(n-1)]

dp = [0]*(1<<n)

for i in reversed(range(1<<n)):
  for j in range(n):
    if (i>>j)&1:
      continue
    for k in range(j+1,n):
      if (i>>k)&1:
        continue
      dp[i] = max(dp[i], dp[i|(1<<j)|(1<<k)]+D[j][k-j-1])

print(dp[0])