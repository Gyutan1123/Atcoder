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

N = II()
n = len(str(N))
dp = [[[0]*(10) for _ in range(2)] for _ in range(10)]

dp[0][0][0] = 1
for i in range(n):
  for j in range(n):
    dp[i+1][1][j] += dp[i][1][j]*9
    dp[i+1][1][j+1] += dp[i][1][j]
    
    ni = ord(str(N)[i])-ord('0')
  
    if ni > 1:
      dp[i+1][1][j] += dp[i][0][j]*(ni-1)
      dp[i+1][1][j+1] += dp[i][0][j] 
    elif ni == 1:
      dp[i+1][1][j] += dp[i][0][j]
    
    if ni == 1:
      dp[i+1][0][j+1] = dp[i][0][j]
    else:
      dp[i+1][0][j] = dp[i][0][j] 

ans = 0
for j in range(10):
  ans += (dp[n][0][j]+dp[n][1][j])*j

print(ans)