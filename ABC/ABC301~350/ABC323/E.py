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

n,x = MI()
T = LI()

inv = pow(n,-1,mod)
inv2 = pow(n-1,-1,mod)

dp = [[0]*(2) for _ in range(x+1)]

dp[0][0] = inv
dp[0][1] = (n-1)*inv

for i in range(x):
  if i+T[0] <= x:
    dp[i+T[0]][0] += dp[i][0]*inv%mod
    dp[i+T[0]][1] += dp[i][0]*(n-1)*inv%mod 
       
  for j in range(1,n):
    if i+T[j] <= x:
      dp[i+T[j]][0] += dp[i][1]*inv2*inv%mod
      dp[i+T[j]][1] += dp[i][1]*inv2*(n-1)*inv%mod

ans = 0
for i in range(x+1):
  if i+T[0] > x:
    ans += dp[i][0]%mod

print(ans%mod)