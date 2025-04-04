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
mod = 10**9 + 7
########################################################

# ダブリング

n,k = MI()
A = LI()

logk = k.bit_length() 

# 手持ちの個数 mod n が jの時に2^i回遷移してもらえる数 
dp = [[-1]*(n) for _ in range(logk)]

for j in range(n):
  dp[0][j] = A[j%mod]

for i in range(logk-1):
  for j in range(n):
    # 2^i回でdp[i][j]もらい、
    # さらに 2^i回でdp[i][(j+dp[i][j])%n] もらう
    dp[i+1][j] = dp[i][j] + dp[i][(j+dp[i][j])%n]

now = 0
i = 0
while k > 0:
  if k & 1:
    now += dp[i][now%n]
  i += 1
  k = k >> 1

print(now)