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

s = tuple(MI())
t = tuple(MI())

if s == t:
  print(0)
elif (s[0]+s[1] == t[0]+t[1] or 
      s[0]-s[1] == t[0]-t[1] or 
      abs(s[0]-t[0])+ abs(s[1]-t[1]) <= 3):
  print(1)
elif (s[0]+s[1]+t[0]+t[1])%2 == 0 or \
      abs(s[0]-t[0]) + abs(s[1]-t[1]) <= 6 or \
      abs(s[0]+s[1]-t[0]-t[1]) <= 3 or \
      abs(s[0]-t[0]-s[1]+t[1]) <= 3:
  print(2)
else:
  print(3)