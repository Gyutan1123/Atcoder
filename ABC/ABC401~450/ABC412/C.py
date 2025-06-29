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
  s = LI()
  now = s[0]
  
  ss = SortedList(s[1:-1])
  
  
  flag = True
  flag2 = True
  cnt = 1
  while ss:
    if s[-1] <= 2*now:
      print(cnt+1)
      flag = False
      break
  
    if 2*now < ss[0]:
      flag2 = False
      break
    
    j = ss.bisect_right(2*now) 
    nxt = ss[j-1]
    if nxt <= 2*now:
      now = nxt
      cnt += 1
      ss.remove(nxt)
  
  if flag2 == False:
    print(-1)
    flag = False

  if flag:
    if s[-1] <= 2*now:
      print(cnt+1)
    else:
      print(-1)
