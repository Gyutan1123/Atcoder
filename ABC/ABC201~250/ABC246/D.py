import sys
import collections, heapq, string, math, itertools, copy
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

a = 0
ans = 10**18


while a*a*a <= n:
  l = -1
  r = 10**6
  while r-l > 1:
    mid = (r+l)//2
    if a**3 + a**2*mid+a*mid**2 + mid**3 >= n:
      r = mid
    else:
      l = mid
  
  ans = min(ans, a**3 + a**2*r+a*r**2 + r**3)
  a += 1
  
print(ans)