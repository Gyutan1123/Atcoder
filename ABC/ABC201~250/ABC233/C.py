import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n,x = MI()
balls = [LI() for _ in range(n)]

ans = 0
# 直積
for p in list(itertools.product(*[balls[i][1:] for i in range(n)])):
  tmp = 1
  for i in range(n):
    tmp *= p[i]

  if tmp == x:
    ans += 1

print(ans)