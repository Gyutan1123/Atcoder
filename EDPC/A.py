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
h = LI()

dp = [float('inf')]*(n)
dp[0] = 0

for i in range(n):
  if i+1 < n:
    dp[i+1] = min(dp[i+1], dp[i]+abs(h[i]-h[i+1]))
  if i+2 < n:
    dp[i+2] = min(dp[i+2], dp[i]+abs(h[i]-h[i+2]))
  
print(dp[-1])