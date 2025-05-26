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

t = II()
for _ in range(t):
  n = II()
  A = []
  for _ in range(2*n):
    A.append(II())
  ans = A[0]
  heap = []
  for i in range(n-1):
    heapq.heappush(heap, -A[2*i+1])
    heapq.heappush(heap, -A[2*i+2])
    ans += -heapq.heappop(heap)
  print(ans)