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
ans = [['?'] * n for _ in range(n)]
for i in range(1,n+1):
  j = n+1-i
  if i <= j:
    if i % 2 == 1:
      for k in range(i,j+1):
        for l in range(i,j+1):
          ans[k-1][l-1] = '#'
    else:
      for k in range(i,j+1):
        for l in range(i,j+1):
          ans[k-1][l-1] = '.'
  
for i in range(n):
  print(''.join(ans[i]))