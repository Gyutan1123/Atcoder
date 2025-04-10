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

n,m = MI()
A = LI()

dp = [[0]*(m+1) for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
  for j in range(1,m+1):
    dp[i+1][j] = max(dp[i][j], dp[i][j-1]+j*A[i])
    
print(dp[n][m])