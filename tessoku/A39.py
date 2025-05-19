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
LR = [LI() for _ in range(n)]
LR.sort(key=lambda x: x[1])
ans = 0
lastTime = 0

for i in range(n):
  l,r = LR[i]
  if lastTime <= l:
    ans += 1
    lastTime = r
print(ans)