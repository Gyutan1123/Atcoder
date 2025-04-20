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

n,m = MI()
LR = [LI() for _ in range(m)]
LR.sort(key=lambda x: (x[0],-x[1]))

s = SortedList()
ans = 0
for l,r in LR:
  ans += s.bisect_left(r)-s.bisect_right(l)
  s.add(r)
print(ans)