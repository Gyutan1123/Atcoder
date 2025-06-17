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

n,W = MI()
A = [LI() for _ in range(n)]


dp = [[float('inf')]*(10001) for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
  w,v = A[i]
  for j in range(10001):
    dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    
    if j+v < 10001:
      dp[i+1][j+v] = min(dp[i+1][j+v], dp[i][j]+w)
      
ans = -1
for j in range(10001):
  if dp[n][j] <= W:
    ans = j
print(ans)