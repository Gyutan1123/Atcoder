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

t = II()
for _ in range(t):
  n = II()
  A = LI()
  A.sort()
  ans = 0  
  s = 0
  for i in range(n):
    s += A[i]
    l = 0
    r = i+1
    while r-l > 1:
      mid = (l+r)//2
      if A[mid]*(i+1) > s:
        r = mid
      else:
        l = mid
    ans = max(ans,i+1-r)
    
  print(ans)