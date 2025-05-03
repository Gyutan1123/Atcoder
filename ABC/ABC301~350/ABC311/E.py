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

h,w,n = MI()

A = set([tuple(LI()) for _ in range(n)])
dp = [[0]*(w) for _ in range(h)]

for i in reversed(range(h)):
  for j in reversed(range(w)):
    if (i+1,j+1) in A:
      dp[i][j] = 0
    elif 0 <= i+1 < h and 0 <= j+1 < w:
      dp[i][j] = min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])+1
    else:
      dp[i][j] = 1

ans = 0
for i in range(h):
  for j in range(w):
    ans += dp[i][j]

print(ans)