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

indices = [[] for _ in range(10**6+1)]

for i, a in enumerate(A):
  indices[a].append(i)

ans = float('inf')
for i in range(n):
  a = A[i]
  
  if len(indices[a]) < 2 or i == indices[a][-1]:
    continue

  j = indices[a][bisect.bisect_right(indices[a], i)]
  ans = min(ans, j-i+1)
  
  
if ans == float('inf'):
  print(-1)
else:
  print(ans)