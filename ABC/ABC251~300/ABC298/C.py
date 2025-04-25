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
q = II()

h = collections.defaultdict(SortedList)
d = collections.defaultdict(SortedSet)

for _ in range(q):
  query = LI()
  if query[0] == 1:
    i,j = query[1:]
    h[j].add(i)
    d[i].add(j)

  if query[0] == 2:
    i = query[1]
    print(*h[i])
  
  if query[0] == 3:
    i = query[1]
    print(*d[i])