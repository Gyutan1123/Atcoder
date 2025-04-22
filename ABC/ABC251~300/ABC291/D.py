import sys
import collections, heapq, string, math, itertools, copy, bisect
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

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

dp = [[0]*2 for _ in range(n+1)]

dp[1][0] = 1
dp[1][1] = 1
AB = [[-1,-1]]
for i in range(n):
  AB.append(LI())
  
for i in range(1,n):
  if AB[i][0] != AB[i+1][0]:
    dp[i+1][0] += dp[i][0]
  
  if AB[i][0] != AB[i+1][1]:
    dp[i+1][1] += dp[i][0]
  
  if AB[i][1] != AB[i+1][0]:
    dp[i+1][0] += dp[i][1]
  
  if AB[i][1] != AB[i+1][1]:
    dp[i+1][1] += dp[i][1]
    
  dp[i+1][0] %= mod
  dp[i+1][0] %= mod
  
print(sum(dp[n]))