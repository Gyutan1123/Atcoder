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

x,a,d,n = MI()

if (x < a and d > 0) or (x > a and d < 0) or d == 0:
  print(abs(x-a))

elif (x > a+(n-1)*d and d > 0) or (x < a+(n-1)*d and d < 0):
  print(abs(x-(a+(n-1)*d)))

else:
  if d > 0:
    l = 1
    r = n
    while r-l > 1:
      mid = (r+l)//2
      if a+(mid-1)*d < x:
        l = mid
      else:
        r = mid
  else:
    l = 1
    r = n
    while r-l > 1:
      mid = (r+l)//2
      if a+(mid-1)*d > x:
        l = mid
      else:
        r = mid


  print(min(abs(x-(a+(r-1)*d)),abs(x-(a+(l-1)*d))))