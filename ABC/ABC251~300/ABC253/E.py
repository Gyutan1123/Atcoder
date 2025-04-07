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

n,m,k = MI()

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,m+1):
  dp[1][i] = 1

for i in range(1,n):
  s = [0]*(m+1)
  for j in range(1,m+1):
    s[j] = s[j-1]+dp[i][j]
  for j in range(1,m+1):
    if k > 0:
      dp[i+1][j] += (s[m] - (s[min(m,j+k-1)]-s[max(0,j-k)]))%mod
    else:
      dp[i+1][j] += s[m]%mod
print(sum(dp[n])%mod)