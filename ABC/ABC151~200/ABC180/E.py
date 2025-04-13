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

#aからbへの距離
def dist(a,b):
  return abs(a[0]-b[0])+abs(a[1]-b[1])+max(0,b[2]-a[2])

n = II()
pos = [LI() for _ in range(n)]

dp = [[float('inf')]*(n) for _ in range(1<<n)]

dp[1][0] = 0

for s in range(1, 1<<n, 2):
  for now in range(n):
    if not (s >> now) & 1:
      continue
    for to in range(n):
      if (s >> to) & 1:
        continue
      
      dp[s^(1<<to)][to] = min(dp[s^(1<<to)][to],
                              dp[s][now]+dist(pos[now],pos[to]))
      
ans = float('inf')

for now in range(1,n):
  ans = min(ans,dp[(1<<n)-1][now]+dist(pos[now],pos[0]))
  
print(ans)
