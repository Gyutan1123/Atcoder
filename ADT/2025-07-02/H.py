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

n,x,y = MI()

dp = [[[float('inf')]*(x+1) for _ in range(n+1)] for _ in range(n+1)]

dp[0][0][0] = 0

for i in range(n):
  a,b = MI()
  for j in range(n):
    for k in range(x+1):    
      dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
      
      if k+a <= x:
        dp[i+1][j+1][k+a] = min(dp[i+1][j+1][k+a], dp[i][j][k]+b)
        
ans = 0
for j in range(1,n+1):
  for k in range(x+1):
    if dp[n][j][k] <= y:
      ans = max(ans, j)

print(min(n,ans+1))
