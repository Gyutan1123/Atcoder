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

h,w,n = MI()

AB = [LI() for _ in range(n)]
usedRows = SortedSet()
usedCols = SortedSet()


for a, b in AB:
  usedRows.add(a)
  usedCols.add(b)

for a,b in AB:
  c = usedRows.bisect_right(a)
  d = usedCols.bisect_right(b)
  print(c,d)
