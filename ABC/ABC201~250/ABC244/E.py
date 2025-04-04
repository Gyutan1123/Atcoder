import sys
import collections, heapq, string, math, itertools, copy
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

n,m,K,s,t,x = MI()

connect = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = MI()
  connect[u].append(v)
  connect[v].append(u)

dp = [[[0]*2 for _ in range(n+1)] for _ in range(K+1)]

dp[0][s][0] = 1

for i in range(K):
  for j in range(1,n+1):
    for to in connect[j]:
      for k in range(2):
        if to == x:
          dp[i+1][to][(k+1)%2] += dp[i][j][k]%mod
        else:
          dp[i+1][to][k] += dp[i][j][k]%mod


print(dp[K][t][0]%mod)