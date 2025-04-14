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

N,M,K = MI()
minv = pow(M,-1,mod)
dp = [[0]*(N+1) for _ in range(K+1)]

dp[0][0] = 1

for i in range(K):
  for j in range(N):
    d = N-j
    for m in range(1,M+1):
      if j+m > N:
        dp[i+1][max(0,N-m+d)] += dp[i][j]*minv%mod
      else:
        dp[i+1][j+m] += dp[i][j]*minv%mod
      
ans = 0
for i in range(1,K+1):
  ans += dp[i][N]%mod

print(ans%mod)