import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

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
x,y = MI()
bento = [LI() for _ in range(n)]

dp = [[[float('inf')]*(y+1) for _ in range(x+1)] for _ in range(n+1)]
dp[0][0][0] = 0

for i in range(n):
  for j in range(x+1):
    for k in range(y+1):
      dp[i+1][j][k] = min(dp[i][j][k], dp[i+1][j][k])
      a,b = bento[i]
      dp[i+1][min(x,j+a)][min(y,k+b)] = min(1 + dp[i][j][k], 
                                            dp[i+1][min(x,j+a)][min(y,k+b)])
  
if dp[n][x][y] != float('inf'):
  print(dp[n][x][y])
else:
  print(-1)