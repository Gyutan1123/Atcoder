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

dp = [float('inf')]*(n+1)
dp[0] = 0
dp[1] = 1

for i in range(n+1):
  if i+1 <= n:
    dp[i+1] = min(dp[i+1],dp[i]+1)
  
  j = 6
  while i+j <= n:
    dp[i+j] = min(dp[i+j], dp[i]+1)
    j *= 6
  
  j = 9
  while i+j <= n:
    dp[i+j] = min(dp[i+j], dp[i]+1)
    j *= 9
    
print(dp[n]) 