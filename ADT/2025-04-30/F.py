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

x1, y1, x2, y2 = MI()

s = set()
for i in range(-3,4):
  for j in range(-3,4):
    xd, yd = x1+i, y1+j
    if (xd-x1)**2 + (yd-y1)**2 == 5:
      s.add((xd, yd))

for i in range(-3,4):
  for j in range(-3,4):
    xd, yd = x2+i, y2+j
    if (xd-x2)**2 + (yd-y2)**2 == 5:
      if (xd, yd) in s:
        print("Yes")
        exit()
print("No")