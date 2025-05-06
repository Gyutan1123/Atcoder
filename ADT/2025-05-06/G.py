import sys
import collections, heapq, string, math, itertools, copy, bisect, functools
from sortedcontainers import SortedSet, SortedList, SortedDict
from atcoder.lazysegtree import LazySegTree

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

INF = 1 << 63
def op(ele1, ele2):
  return min(ele1, ele2)


def mapping(func, ele):
  return func + ele


def composition(func_upper, func_lower):
  return func_upper + func_lower

e = INF
id_ = 0
segtree = LazySegTree(op, e, mapping, composition,id_, [0]*200000)

now = 200000-1
r = 200000

q = II()
for _ in range(q):
  query = LI()
  if query[0] == 1:
    now -= 1
  if query[0] == 2:
    segtree.apply(now+1, r, query[1])
  
  if query[0] == 3:
    l = segtree.min_left(r, lambda x: x >= query[1])
    print(r-l)
    r = l