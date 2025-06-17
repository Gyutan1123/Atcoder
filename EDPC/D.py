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

dp = [[-1]*(W+1) for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
  for j in range(W+1):
    w,v = A[i]
    dp[i+1][j] = max(dp[i+1][j], dp[i][j])  
    if w+j <= W:
      dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j]+v)

    
print(max(dp[-1]))