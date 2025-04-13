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

n,x,y = MI()
A = LI()

dpx = [[False]*(20000+1)]
dpy = [[False]*(20000+1)]


dpx[0][A[0]+10000] = True
dpy[0][10000] = True

for i in range(1,n):
  if i % 2 == 1:
    dpy.append([False]*(20000+1))
    for j in range(20001):
      dpy[-1][j] = dpy[-1][j]
      if 0 <= j-A[i] <= 20000:
        dpy[-1][j] = dpy[-1][j] | dpy[-2][j-A[i]]
      if 0 <= j+A[i] <= 20000:
        dpy[-1][j] = dpy[-1][j] | dpy[-2][j+A[i]]
  else:
    dpx.append([False]*(20000+1))
    for j in range(20001):
      dpx[-1][j] = dpx[-1][j]
      if 0 <= j-A[i] <= 20000:
        dpx[-1][j] = dpx[-1][j] | dpx[-2][j-A[i]]
      if 0 <= j+A[i] <= 20000:
        dpx[-1][j] = dpx[-1][j] | dpx[-2][j+A[i]]
        
if dpx[-1][x+10000] and dpy[-1][y+10000]:
  print('Yes')
else:
  print('No')