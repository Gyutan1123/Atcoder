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
s = SortedList()

AB = [sorted(LI()) for _ in range(n)]

AB.sort(key=lambda x: x[0])

ans = 'No'
for a,b in AB:
  i = s.bisect_left(a)
  j = s.bisect_right(b)
  if i < j:
    ans = 'Yes'
    break 
  s.add(b)

print(ans)