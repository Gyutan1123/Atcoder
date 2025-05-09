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

n,m = MI()
L = LI()

l = max(L)-1
r = 10**18

while r-l > 1:
  mid = (l+r)//2
  s = 0
  line = 1
  for i in range(n):
    if s+L[i] <= mid:
      s += L[i]+1
    else:
      s = L[i]+1
      line += 1
  if line <= m:
    r = mid
  else:
    l = mid
print(r)