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
A = LI()

dp = [[0]*2 for _ in range(n)]
  
ans = float('inf')

dp[0][0] = 0
dp[0][1] = float('inf')

for i in range(n-1):
  dp[i+1][0] = dp[i][1]
  dp[i+1][1] = A[i+1]+min(dp[i])
  
ans = min(ans,dp[n-1][1])

dp[0][1] = A[0]
dp[0][0] = float('inf')

for i in range(n-1):
  dp[i+1][0] = dp[i][1]
  dp[i+1][1] = A[i+1]+min(dp[i])
  
ans = min(ans,dp[n-1][1], dp[n-1][0])

print(ans)