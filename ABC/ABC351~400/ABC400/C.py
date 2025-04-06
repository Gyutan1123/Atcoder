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

a = 1
ans = 0
while pow(2,a) <= n:
  l = 0
  r = 10**10
  while r-l > 1:
    mid = (r+l)//2
    if pow(2,a)*mid**2 > n:
      r = mid
    else:
      l = mid
  if l %2 == 0:
    ans += l//2
  else:
    ans += l//2 + 1
  a += 1
  
print(ans)