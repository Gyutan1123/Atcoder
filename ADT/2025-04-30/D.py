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
A = [list(SI()) for _ in range(n)]

D = [(1,0), (0,1), (-1,0), (0,-1),(1,1), (1,-1), (-1,1), (-1,-1)]

ans = 0
for i in range(n):
  for j in range(n):
    for d in D:
      tmp = [A[i][j]]
      ni, nj = i, j
      for k in range(n-1):
        ni += d[0]
        nj += d[1]

        if ni < 0:
          ni = n-1
        if ni >= n:
          ni = 0

        if nj < 0:
          nj = n-1
        if nj >= n:
          nj = 0

        tmp.append(A[ni][nj])
      
      ans = max(ans, int("".join(tmp)))
print(ans)