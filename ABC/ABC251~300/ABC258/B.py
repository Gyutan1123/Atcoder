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

D = [(1,0),(-1,0),(0,1),(0,-1),
     (1,1),(1,-1),(-1,1),(-1,-1)]

ans = 0
for i in range(n):
  for j in range(n):
    for d in D:
      tmp = []
      for k in range(n):
        tmp.append(A[(i+d[0]*k)%n][(j+d[1]*k)%n])
      ans = max(ans, int(''.join(tmp)))

print(ans)