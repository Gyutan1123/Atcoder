import sys
import collections, heapq, string, math, itertools
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())


sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

K = II()
if K % 9 != 0:
  print(0)
  exit()
  
dp = [[0]*10 for _ in range(K+1)]
dp[0][0] = 1

for i in range(1,K+1):
  for j in range(1,10):
    if i - j >= 0:
      dp[i][j] = sum(dp[i-j]) % mod
  
print(sum(dp[K])%mod)
