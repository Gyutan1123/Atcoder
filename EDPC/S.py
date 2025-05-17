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

K = SI()
D = II()

dp = [[[0]*D  for _ in range(2)] for _ in range(len(K)+1)]

dp[0][0][0] = 1

for i in range(len(K)):
  for j in range(D):
    for k in range(10):
      dp[i+1][1][(j+k)%D] += dp[i][1][j]
      dp[i+1][1][(j+k)%D] %= mod
    
    ni = ord(K[i])-ord('0')
    for k in range(ni):
      dp[i+1][1][(j+k)%D] += dp[i][0][j]
      dp[i+1][1][(j+k)%D] %= mod
    
    dp[i+1][0][(j+ni)%D] = dp[i][0][j]
    
print(dp[len(K)][0][0]+dp[len(K)][1][0]-1)
  