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
n,m = MI()

R = [LI() for _ in range(n)]
Z = [0]*n
for i in range(n):
  S = R[i][2:]
  for s in S:
    if s == 0:
      Z[i] += 1

dp = [0]*(2*m+1)

for i in reversed(range(m)):
  tmp1 = float('inf')
  for j in range(n):
    c = R[j][0]
    p = R[j][1]
    z = Z[j]
    S = R[j][2:]
  
    tmp2 = c*p/(p-z)

    for s in S:
      if s == 0:
        continue
      tmp2 += 1/(p-z)*dp[i+s]
      
    tmp1 = min(tmp1, tmp2)
  
  dp[i] = tmp1

print(dp[0])