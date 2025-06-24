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

n = SI()

i = n.find('.')
y = int(n[i+1:])
x = int(n[:i])
if 0 <= y <= 2:
  print(f'{x}-')
elif 3 <= y <= 6:
  print(f'{x}')
elif 7 <= y <= 9:
  print(f'{x}+')
