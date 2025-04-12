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
mod = 10**9 + 7
########################################################

n = II()
a = LI()
a = SortedSet(a)
l = 0
r = 10**9

while r-l > 1:
  mid = (r+l)//2
  read = a.bisect_right(mid)
  buy = n-a.bisect_right(mid) 

  buy += read-len(set(a[:read]))
  read = len(set(a[:read]))
  if read + buy//2 >= mid:
    l = mid
  else:
    r = mid

print(l)
