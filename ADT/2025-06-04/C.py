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
sn = str(n)
if n <= 10**3-1:
  print(sn)
elif n <= 10**4-1:
  print(sn[:-1]+"0")
elif n <= 10**5-1:
  print(sn[:-2]+"00")
elif n <= 10**6-1:
  print(sn[:-3]+"000")
elif n <= 10**7-1:
  print(sn[:-4]+"0000")
elif n <= 10**8-1:
  print(sn[:-5]+"00000")
elif n <= 10**9-1:
  print(sn[:-6]+"000000")
