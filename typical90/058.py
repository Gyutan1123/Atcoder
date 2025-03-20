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

n,k = MI()
logk = (k-1).bit_length() # 2^(logk) >= k となる最小の整数
dp = [[i for i in range(100000)] for _ in range(logk+1)]

for j in range(100000):
  dp[0][j] = (dp[0][j]+sum(map(int, str(dp[0][j]))))%100000
  
for i in range(logk):
  for j in range(100000):
    dp[i+1][j] = dp[i][dp[i][j]]

ans = n
for i in range(logk+1):
  if k >> i & 1:
    ans = dp[i][ans]
print(ans)