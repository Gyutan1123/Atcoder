import sys
import collections, heapq, string, math, itertools

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(LS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n = II()
LR = [LI() for _ in range(n)]

ans = 0
for i in range(n):
  for j in range(i+1,n):
    tmp = 0
    li,ri = LR[i]
    lj,rj = LR[j]
    for k in range(lj,rj+1):
      if li > k:
        tmp += ri-li+1
      elif li <= k and k < ri:
        tmp += ri-k
    ans += tmp/((ri-li+1)*(rj-lj+1))
    
print(ans) 