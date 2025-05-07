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
ans = 0
s = set()
for _ in range(m):
  u,v = MI()
  u,v = min(u,v),max(u,v)
  if u == v:
    ans += 1
  elif (u,v) not in s:
    s.add((u,v))
  else:
    ans += 1
print(ans)