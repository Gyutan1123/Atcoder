import sys
import collections, heapq, string, math, itertools, copy, bisect
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

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
inv = pow(5,-1,mod)
d = dict()
d[n] = 1
def dp(i):
  global n
  if i > n:
    return 0
  elif i in d:
    return d[i]
  else:
    d[i] = (inv*((dp(2*i)+dp(3*i)+dp(4*i)+dp(5*i)+dp(6*i))%mod))%mod
    return d[i]
  
print(dp(1))