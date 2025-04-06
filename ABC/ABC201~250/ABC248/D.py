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
A = LI()
q = II()
d = collections.defaultdict(list)
for i in range(n):
  d[A[i]].append(i+1)
for _ in range(q):
  l,r,x = MI()
  print(bisect.bisect_right(d[x],r)-bisect.bisect_left(d[x],l))