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

l,n1,n2 = MI()

l1 = [LI() for _ in range(n1)]
l2 = [LI() for _ in range(n2)]

ans = 0

x1 = 0
x2 = 0
i2 = 0
for v1,k1 in l1:
  if x1 < x2:
    if v1 == v2:
      ans += min(k1,x2-x1)

  x1 += k1
  
  while x2 < x1 and i2 < n2:
    v2,k2 = l2[i2]
    i2 += 1
    if v2 == v1:
      ans += min(k2, x1-x2)
    x2 += k2

print(ans)