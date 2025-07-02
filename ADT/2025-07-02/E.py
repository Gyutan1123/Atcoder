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
S = SI()
visited = set()

visited.add((0,0))

now = (0,0)
ans = 'No'
for s in S:
  if s == 'U':
    now = (now[0], now[1] + 1)
  elif s == 'D':
    now = (now[0], now[1] - 1)
  elif s == 'L':
    now = (now[0] - 1, now[1])
  elif s == 'R':
    now = (now[0] + 1, now[1])
      
  if now in visited:
    ans = 'Yes'
  
  visited.add(now)
  
print(ans)
