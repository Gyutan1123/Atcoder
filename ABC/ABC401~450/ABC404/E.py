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
C = [0]+LI()
A = [0]+LI()

ans = 0
for i in reversed(range(1,n)):
  if A[i] <= 0:
    continue
  flag = False
  for j in range(i-C[i], i):
    if A[j] > 0:
      flag = True
      ans += 1
      break
  if not flag:
    m = float('inf')
    for j in range(i-C[i], i):
      if j-C[j] < m:
        m = j-C[j]
        to = j
    A[to] += 1
    ans += 1

print(ans)