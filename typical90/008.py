import sys
import collections, heapq, string
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

mod = 10**9 + 7
########################################################

n = II()
s = SI()

mod = 10**9 + 7

dp = [[0]*(n+1) for _ in range(8)]

str = '?atcoder'

for j in range(n+1):
  dp[0][j] = 1

for i in range(1,8):
  for j in range(n):
    if s[j] == str[i]:
      dp[i][j+1] = (dp[i][j] + dp[i-1][j]) % mod
    else:
      dp[i][j+1] = dp[i][j] % mod

print(dp[7][n] % mod)