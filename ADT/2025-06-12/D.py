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
T = SI()

dxdy = (1,0)
now = (0,0)
for i in range(n):
  t = T[i]
  if t == 'S':
    x,y = now
    now = (x + dxdy[0], y + dxdy[1])
  elif t == 'R':
    if dxdy == (1, 0):
      dxdy = (0, -1)
    elif dxdy == (0, -1):
      dxdy = (-1, 0)
    elif dxdy == (-1, 0):
      dxdy = (0, 1)
    elif dxdy == (0, 1):
      dxdy = (1, 0)
      
print(now[0], now[1])
