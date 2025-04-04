import sys
import collections, heapq, string, math, itertools, copy
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

q = II()

A = SortedList()
for _ in range(q):
  query = LI()
  if query[0] == 1:
    A.add(query[1])
  if query[0] == 2:
    x,k = query[1:]
    i = A.bisect_right(x)
    if i >= k:
      print(A[i-k])
    else:
      print(-1)
      
  if query[0] == 3:
    x,k = query[1:]
    i = A.bisect_left(x)
    if (len(A)-i) >= k:
      print(A[i+k-1])
    else:
      print(-1)