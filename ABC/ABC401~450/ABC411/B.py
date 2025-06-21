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
d = LI()

ans = [[] for _ in range(n-1)]

for i in range(n-1):
  for j in range(i+1,n):
    tmp = 0
    for k in range(i,j):
      tmp += d[k]
    ans[i].append(tmp)

for i in range(n-1):
  print(*ans[i])