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

n,h,m = MI()
AB = [LI() for _ in range(n)]

dp = [[0]*(m+1) for _ in range(h+1)]

dp[0][0] = 0
ans = 0
for i in range(h+1):
  for j in range(m+1):
    ans = max(ans, dp[i][j])
    if dp[i][j] < n:
      a,b = AB[dp[i][j]]
      if i+a <= h:
        dp[i+a][j] = max(dp[i+a][j], dp[i][j]+1)
      if j+b <= m:
        dp[i][j+b] = max(dp[i][j+b], dp[i][j]+1)

print(ans)