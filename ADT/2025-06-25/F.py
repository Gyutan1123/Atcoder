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
mg = II()
connect1 = [[False]*(n+1) for _ in range(n+1)]
for _ in range(mg):
  a, b = MI()
  connect1[a][b] = True
  connect1[b][a] = True
mh = II()
connect2 = [[False]*(n+1) for _ in range(n+1)]
for _ in range(mh):
  a, b = MI()
  connect2[a][b] = True
  connect2[b][a] = True

A = [LI() for _ in range(n-1)]

ans = float('inf')
for p in itertools.permutations(range(1,n+1)):
  tmp = 0
  for i in range(n):
    for j in range(i+1,n):
      if connect1[p[i]][p[j]] != connect2[i+1][j+1]:
        tmp += A[i][j-i-1]
  ans = min(ans, tmp)

print(ans)