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

n,m,k = MI()

Edge = [tuple(LI()) for _ in range(m)]
E = LI()

dp = [float('inf')]*(n+1)

dp[1] = 0

for i in range(k):
  a,b,c = Edge[E[i]-1]
  dp[b] = min(dp[a]+c,dp[b])

if dp[n] != float('inf'):
  print(dp[n])
else:
  print(-1)