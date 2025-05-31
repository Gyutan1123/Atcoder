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
from atcoder import fenwicktree
n = II()
A = LI()

bit = fenwicktree.FenwickTree(10**8+1)
s = SortedList()

ans = 0
for i in reversed(range(n)):
  a = A[i]
  
  S = bit.sum(a+1, 10**8+1)
  l = len(s)-s.bisect_right(a)
  
  ans += S-a*l
  
  bit.add(a, a)
  s.add(a)
  
print(ans)