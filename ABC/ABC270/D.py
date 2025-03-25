import sys
import collections, heapq, string, math, itertools, copy

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n,k = MI()
A = LI()

dp = [[0]*2 for _ in range(n+1)]

for i in range(1,n+1):
  for a in A:
    if a > i:
      break
    # 山からa個とる。
    # 相手はその後dp[i-a][0or1] 個とる。
    dp[i][0] = max(dp[i][0], a+(i-a-dp[i-a][1]))
    dp[i][1] = max(dp[i][1], a+(i-a-dp[i-a][0]))

print(dp[n][0])