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

n,m = MI()
A = LI()
A.sort()
rooms = [LI() for _ in range(m)]
rooms.sort()

dp = [[float('inf') ]*(n+1) for _ in range(m+1)]
dp[0][0] = 0

# 今見ている部屋までで入れられる人数
idx = 0

for i in range(m):
  r,b,c = rooms[i]
  while idx < n and A[idx] <= r:
    idx += 1
  for j in range(n+1):
    dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    
    # この部屋に入れられる人数
    cnt = idx-j
    if cnt > 0 and cnt <= b and j+cnt <= n:
      dp[i+1][j+cnt] = min(dp[i+1][j+cnt],dp[i][j]+c)
    elif cnt > b and j+b <= n:
      dp[i+1][j+b] = min(dp[i+1][j+b],dp[i][j]+c)


if dp[m][n] == float('inf'):
  print(-1)
else:
  print(dp[m][n])
