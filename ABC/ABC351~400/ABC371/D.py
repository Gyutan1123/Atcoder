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
mod = 10**9 + 7
########################################################

n = II()
X = LI()
P = LI()
Q = II()

SP = [0]
for p in P:
  SP.append(SP[-1] + p)

for _ in range(Q):
  l,r = MI()
  
  i = bisect.bisect_left(X,l)
  j = bisect.bisect_right(X,r)
  
  print(SP[j]-SP[i])