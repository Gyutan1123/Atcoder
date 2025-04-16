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

n,p = MI()

inv = pow(100,-1,mod)

dp = [0]*(n+1)
dp[0] = 0
dp[1] = 1

for i in range(2,n+1):
  dp[i] = (p*inv*(1+dp[i-2])+(100-p)*inv*(1+dp[i-1]))%mod
  
  
print(dp[n]%mod)