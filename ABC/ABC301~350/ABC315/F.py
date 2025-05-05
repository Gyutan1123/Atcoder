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


def dist(x,y):
  return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5

n = II()
P = [LI() for _ in range(n)]

dp = [[float('inf')]*(50) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n-1):
  for j in range(50):
    dp[i+1][j] = min(dp[i+1][j], dp[i][j]+dist(P[i], P[i+1]))
    for k in range(1,50):
      if j-k >= 0 and i-k >= 0:
        dp[i+1][j] = min(dp[i+1][j], dp[i-k][j-k]+dist(P[i+1],P[i-k]))

    
ans = float('inf')
for i in range(50):
  if i == 0:
    ans = min(ans, dp[n-1][i])
  else:
    ans = min(ans, dp[n-1][i]+2**(i-1))     
    
print(ans)