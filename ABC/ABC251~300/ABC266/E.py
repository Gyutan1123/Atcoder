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

n = II()

dp = [[0]*7 for _ in range(n+1)]

for j in range(1,7):
  dp[n][j] = j
  
for i in reversed(range(1,n+1)):
  for j in range(1,7):
    dp[i-1][j] = max(sum(dp[i])/6, j)
  
print(dp[0][1])