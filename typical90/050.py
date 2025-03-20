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

n,l = MI()
dp = [0]*(n+1)
dp[0] = 1

for i in range(1,n+1):
  if i-l >= 0:
    dp[i] = (dp[i-1]+dp[i-l])%mod
  else:
    dp[i] = dp[i-1]%mod
    
print(dp[n]%mod)