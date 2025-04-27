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

n,m,x = MI()
book = [LI() for _ in range(n)]
ans = float('inf')
for i in range(1<<n):
  tmp = [0]*m
  p = 0
  for j in range(n):
    if (i>>j)&1:
      p += book[j][0]
      for k in range(m):
        tmp[k] += book[j][k+1]
      
  if min(tmp) >= x:
    ans = min(ans,p)

if ans < float('inf'):
  print(ans)
else:
  print(-1)