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

n,k = MI()
A = LI()
A.sort(reverse=True)

l = 0
r = 10**9+1

while r-l > 1:
  mid = (l+r)//2
  cnt = 0
  for a in A:
    cnt += (a+mid-1)//mid - 1
  if cnt <= k:
    r = mid
  else:
    l = mid

print(r)