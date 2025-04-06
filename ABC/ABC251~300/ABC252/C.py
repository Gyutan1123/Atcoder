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

n = II()
s = [SI() for _ in range(n)]
ans = float('inf')
for i in range(10):
  t = SortedSet()
  for j in range(n):
    for k in range(10):
      if s[j][k] == str(i):
        if not k in t:
          t.add(k)
        else:
          l = 1
          while k+10*l in t:
            l += 1
          t.add(k+10*l)
          
  ans = min(ans,t[-1])
          
print(ans)