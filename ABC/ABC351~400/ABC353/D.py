import sys
import collections, heapq, string, math, itertools, copy, bisect, functools
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
A = LI()

accum = [0]
for i in range(n):
  accum.append((accum[-1] + A[i]) % mod)
s = 0
for i in range(n):
  s += pow(10, len(str(A[i])),mod)

ans = 0
for i in range(n-1):
  s -= pow(10,len(str(A[i])),mod)
  ans += A[i]*s
  ans %= mod
  ans += (accum[n]-accum[i+1])%mod
  ans %= mod
  
print(ans%mod)  
