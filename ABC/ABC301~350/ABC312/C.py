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

n,m = MI()
A = LI()
B = LI()


l = 0
r = 10**15

while r-l > 1:
  cntA = 0
  cntB = 0
  mid = (l+r)//2
  for i in range(n):
    if A[i] <= mid:
      cntA += 1
  for i in range(m):
    if B[i] >= mid:
      cntB += 1
      
  if cntA >= cntB:
    r = mid
  else:
    l = mid

print(r)