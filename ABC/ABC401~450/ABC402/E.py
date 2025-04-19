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

n,x = MI()

dp = [[0]*(x+1) for _ in range(1<<n)]

P = [LI() for _ in range(n)]

for j in range(x+1):
  for i in range(1<<n):
    for k in range(n):
      if (i>>k) & 1 == 0:
        continue
      
      if j-P[k][1] < 0:
        continue
      
      dp[i^(1<<k)][j] = max(dp[i^(1<<k)][j], 
                            P[k][2]*(dp[i][j-P[k][1]]+P[k][0])/100+(100-P[k][2])*dp[i^(1<<k)][j-P[k][1]]/100)
ans = 0
for i in range(1<<n):
  for j in range(x+1):
    ans = max(ans,dp[i][j])
print(ans)