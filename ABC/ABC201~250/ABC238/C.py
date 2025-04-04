import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

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

l = len(str(n))

ans = 0
for i in range(l-1):
  ans += ((10**(i+1)-10**i)*(10**(i+1)-10**i+1)//2)%mod
ans += ((n-10**(l-1)+1)*(n-10**(l-1)+2)//2)%mod
print(ans%mod)