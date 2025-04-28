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

dp = [[0]*2 for _ in range(n+1)]
dp[0][0] = 0
dp[0][1] = 0

for i in range(1,n+1):
  x,y = MI()
  if x == 0:
    dp[i][0] = max(dp[i-1][0], 
                   dp[i-1][0]+y,
                   dp[i-1][1]+y)
    
    dp[i][1] = dp[i-1][1]
  if x == 1:
    dp[i][0] = dp[i-1][0]
    dp[i][1] = max(dp[i-1][1],dp[i-1][0]+y)

print(max(dp[n][0], dp[n][1]))