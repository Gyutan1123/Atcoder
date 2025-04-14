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

n = II()


d = dict()

d[0] = 1

def f(k):
  if k in d:
    return d[k]
  
  if k//2 in d:
    fk2 = d[k//2]
  else:
    fk2 = f(k//2)
    d[k//2] = fk2
  
  if k//3 in d:
    fk3 = d[k//3]
  else:
    fk3 = f(k//3)
    d[k//3] = fk3

  return fk2+fk3

print(f(n))