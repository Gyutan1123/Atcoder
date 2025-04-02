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

n,d = MI()

if d == 1:
  print(2*(pow(2,n,mod)-2)%mod)
  exit()

dp = [0]*n

for i in reversed(range(n-1)):
  h = n-i
  if d == 2*(h-1) or d == 2*(h-1)-1:
    dp[i] += 2*pow(2,2*h-4,mod)
  if d < 2*(h-1)-1:
    # 子孫内で完結
    dp[i] += 2*dp[i+1]%mod
    
    # 両方の子孫+自分
    dp[i] += 2*(min(h-1,d-1)-max(1,d-h+1)+1)*pow(2,d-2,mod)%mod
    
    # 自分+片方の子孫のみ
    if d <= h-1:
      dp[i] += 2*pow(2,d,mod)
    
print(dp[0]%mod)