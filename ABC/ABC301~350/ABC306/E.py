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

n,k,q = MI()

d = [0]*(n+1)
s = SortedList([0]*n)
ans = 0
for i in range(q):
  x,y = MI()
  t = s[-k]
  
  aOld = d[x]
  d[x] = y
  s.add(y)
  s.discard(aOld)

  if aOld >= t and y >= t:
    ans -= aOld
    ans += y
  elif aOld >= t and y < t:
    ans -= aOld
    ans += s[-k]
  elif aOld < t and y >= t:
    ans -= t
    ans += y
    
  print(ans)