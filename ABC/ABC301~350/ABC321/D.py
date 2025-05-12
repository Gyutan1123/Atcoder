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

n,m,p = MI()
A = LI()
B = LI()

A.sort()
B.sort()

S = [0]
for i in range(m):
  S.append(S[-1] + B[i])

ans = 0
for i in range(n):
  l = -1
  r = m
  while r-l > 1:
    mid = (l + r) // 2
    if A[i] + B[mid] >= p:
      r = mid
    else:
      l = mid
  ans += p*(m-r)
  ans += A[i]*r+S[r]
print(ans)
