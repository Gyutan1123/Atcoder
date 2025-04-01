import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 998244353
########################################################
s = SI()
n = len(s)

fact = dict()
finv = dict()
fact[0] = 1
finv[0] = 1
for i in range(n+1):
  fact[i+1] = (i+1)*fact[i]
  finv[i] = pow(fact[i],mod-2,mod)
  fact[i] %= mod

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

d = collections.defaultdict(int)
for i in range(n):
  d[s[i]] += 1

dp = [[0]*(n+1) for _ in range(27)]
for i in range(27):
  dp[i][0] = 1

for i in range(26):
  x = d[ascii_lowercase[i]]
  for j in range(1,n+1):
    for k in range(x+1):
      if j-k >= 0:
        dp[i+1][j] += (dp[i][j-k]*(fact[j])*finv[j-k]*finv[k])%mod
      else:
        break
print(sum(dp[26][1:])%mod)