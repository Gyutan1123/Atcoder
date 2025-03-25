import sys
import collections, heapq, string, math, itertools, copy

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 998244353
########################################################

n = II()
S = SI()

X = 'ABCDEFGHIJ'

dp = [[[0]*(2**10) for _ in range(10) ] for _ in range(n+1)]


for i in range(n):
  # i文字目を選ばない
  for j in range(10):
    for k in range(2**10):
      dp[i+1][j][k] = dp[i][j][k]%mod
    
  # i文字目を選ぶ
  index = X.index(S[i])
  for k in range(2**10):
    if (k >> index) & 1 == 0:
      continue
    
    if k == 1 << index:
      dp[i+1][index][k] += 1
    
    dp[i+1][index][k] += dp[i][index][k]%mod
    
    for j in range(10):
      dp[i+1][index][k] += dp[i][j][k-(1<<index)]%mod
    
ans = 0
for j in range(10):
  for k in range(2**10):
    ans += dp[n][j][k]%mod
    
print(ans%mod)