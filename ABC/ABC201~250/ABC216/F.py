import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

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
A = LI()
B = LI()

AB = [(A[i],B[i]) for i in range(n)]
AB.sort()

dp = [[0]*(5001) for _ in range(n+1)]
dp[0][0] = 1

dp2 = [[0]*(5001) for _ in range(n+1)]
dp2[0][0] = 1
for i in range(n):
  b = AB[i][1]
  for j in range(5001):
    dp2[i+1][j] += dp2[i][j] % mod
    if j - b >= 0:
      dp2[i+1][j] += dp2[i][j-b] % mod

for i in range(1,n+1):
  # i個目を使わない
  for j in range(5001):
    dp[i][j] += dp[i-1][j] % mod
  
  # i個目を使う
  a,b = AB[i-1]
  for j in range(a-b+1):
    dp[i][j+b] += dp2[i-1][j] % mod
    

ans = 0
for j in range(1,5001):
  ans += dp[n][j] % mod
  
print(ans%mod)