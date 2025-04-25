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
mod = 998244353
########################################################

n,a,b,p,q = MI()

pinv = pow(p,-1,mod)
qinv = pow(q,-1,mod)


dp = [[[0]*2 for _ in range(n+1)] for _ in range(n+1)]

for j in range(n+1):
  dp[j][n][0] = 0
  dp[n][j][1] = 1


for i in reversed(range(n)):
  for j in reversed(range(n)):
    for k in range(1,p+1):
      dp[i][j][0] += (pinv*dp[min(i+k,n)][j][1])%mod
    for k in range(1,q+1):
      dp[i][j][1] += (qinv*dp[i][min(j+k,n)][0])%mod

print(dp[a][b][0]%mod)