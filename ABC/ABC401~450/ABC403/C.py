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

n,m,q = MI()

a = [set() for _ in range(n)]
aa = [-1]*(n)

for _ in range(q):
  query = LI()
  if query[0] == 1:
    a[query[1]-1].add(query[2]-1)
  elif query[0] == 2:
    aa[query[1]-1] = True
  else:
    if aa[query[1]-1] == True:
      print("Yes")
    elif query[2]-1 in a[query[1]-1]:
      print("Yes")
    else:
      print("No")
