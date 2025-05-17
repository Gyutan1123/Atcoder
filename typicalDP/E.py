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

d = II()
N = SI()
n = len(N)

dp = [[[0]*d for _ in range(2)] for _ in range(n+1)]
dp[0][0][0] = 1

for i in range(n):
  for j in range(d):
    for k in range(10):
      dp[i+1][1][(j+k)%d] += dp[i][1][j]
      dp[i+1][1][(j+k)%d] %= mod
    
    ni = ord(N[i])-ord('0')
    
    for k in range(ni):
      dp[i+1][1][(j+k)%d] += dp[i][0][j]
      dp[i+1][1][(j+k)%d] %= mod
    
    dp[i+1][0][(j+ni)%d] = dp[i][0][j]
    
print(dp[n][0][0]+dp[n][1][0]-1)