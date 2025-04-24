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

n,m = MI()

ans = float('inf')

a = 1
while a < int(m**0.5)+100 and a <= n:
  l = a
  r = n

  while r-l > 1:
    mid = (r+l)//2
    if a*mid < m:
      l = mid
    else:
      r = mid
  
  if a*r >= m:
    ans = min(ans, a*r)

  a += 1

if ans < float('inf'):
  print(ans)
else:
  print(-1)