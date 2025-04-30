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
def cmp(x,y):
  a1,b1,i1 = x
  a2,b2,i2 = y
  
  if a1*(a2+b2) > a2*(a1+b1):
    return -1
  elif a1*(a2+b2) < a2*(a1+b1):
    return 1
  elif i1 > i2:
    return 1
  elif i1 < i2:
    return -1

n = II()

AB = [tuple(LI()+[i+1]) for i in range(n)]
AB.sort(key=functools.cmp_to_key(cmp))

ans = [AB[i][2] for i in range(n)]
print(*ans)