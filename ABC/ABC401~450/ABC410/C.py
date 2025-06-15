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

n,q = MI()
A = [(i+1) for i in range(n)]

shift = 0
for _ in range(q):
  query = LI()
  if query[0] == 1:
    p,x = query[1:]
    A[(p-1+shift)%n] = x
  elif query[0] == 2:
    print(A[(query[1]-1+shift)%n])
  else:
    shift += query[1]
