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
a = LI()

kuda = collections.deque()
ans = 0
for i in range(n):
  if kuda:
    now = kuda.popleft()
    if now[0] == a[i]:
      if now[1]+1 < a[i]:
        kuda.appendleft((now[0], now[1]+1))
        ans += 1
      else:
        ans -= now[1]
    else:
      kuda.appendleft(now)
      kuda.appendleft((a[i], 1))
      ans += 1
  else:
    kuda.appendleft((a[i], 1))
    ans += 1
  
  print(ans)