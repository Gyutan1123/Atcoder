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

t = II()
for _ in range(t):
  n = II()
  P = LI()
  
  if P == list(range(1, n+1)):
    print(0)
    continue
  if P[0] == n and P[-1] == 1:
    print(3)
    continue  
  flag = False
  tmpMax = -1
  for i in range(n):
    tmpMax = max(tmpMax, P[i])
    if tmpMax == i+1 and P[i] == i+1:
      flag = True
      break
  if flag:
    print(1)
  else:
    print(2)
