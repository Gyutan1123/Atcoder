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
A = LI()

s = SortedSet()
for i in range(n):
  if A[i] == i+1:
    s.add(i)

ans = 0
for i in range(n):
  ai = A[i]
  if ai > i+1 and A[ai-1] == i+1:
    ans += 1
  if ai == i+1:
    ans += len(s)-s.bisect_right(i)

print(ans)