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

n,k = MI()
h = LI()
dp = [float('inf')]*(n)
dp[0] = 0
for i in range(n):
  for j in range(1,k+1):
    if i+j < n:
      dp[i+j] = min(dp[i+j], dp[i]+abs(h[i]-h[i+j]))

print(dp[n-1])