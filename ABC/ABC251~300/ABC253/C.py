import sys
import collections, heapq, string, math, itertools, copy
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

q = II()

d = collections.defaultdict(int)
s = SortedSet()

for _ in range(q):
  query = LI()
  if query[0] == 1:
    d[query[1]] += 1
    s.add(query[1])

  if query[0] == 2:
    x,c = query[1:]
    d[x] -= min(c, d[x])
    if d[x] == 0:
      s.discard(x)
    
  if query[0] == 3:
    print(s[-1]-s[0])
