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

n,m = MI()
X = LI()
C = collections.defaultdict(int)
for _ in range(m):
  c,y = MI()
  C[c] = y

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
  dp[i+1][0] = max(dp[i])
  for j in range(1,i+2):
    dp[i+1][j] = dp[i][j-1]+X[i]+C[j]

print(max(dp[n]))