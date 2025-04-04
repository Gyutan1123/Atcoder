import sys
import collections, heapq, string, math, itertools, copy
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
mod = 998244353
########################################################

n = II()

dp = [[0]*10 for _ in range(n+1)]

for j in range(1,10):
  dp[1][j] = 1

for i in range(2,n+1):
  for j in range(1,10):
    if 2 <= j <= 8:
      dp[i][j] = (dp[i-1][j]+dp[i-1][j-1]+dp[i-1][j+1])%mod
    elif j == 1:
      dp[i][j] = (dp[i-1][j]+dp[i-1][j+1])%mod
    elif j == 9:
      dp[i][j] = (dp[i-1][j]+dp[i-1][j-1])%mod
    
print(sum(dp[n])%mod)