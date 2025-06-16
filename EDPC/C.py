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

ABC = [LI() for _ in range(n)]

dp = [[-float('inf')]*3 for _ in range(n)]
dp[0] = [ABC[0][0], ABC[0][1], ABC[0][2]]

for i in range(1,n):
  a,b,c = ABC[i]
  dp[i][0] = max(dp[i-1][1]+a, dp[i-1][2]+a)
  dp[i][1] = max(dp[i-1][0]+b, dp[i-1][2]+b)
  dp[i][2] = max(dp[i-1][0]+c, dp[i-1][1]+c)
  
print(max(dp[n-1]))