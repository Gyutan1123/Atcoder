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

s = SI()
t = SI()

if s == t:
  print('Yes')
  exit()
else:
  for i in range(len(s)-1):
    tmp = list(s)
    tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
    if ''.join(tmp) == t:
      print('Yes')
      exit()

print('No')