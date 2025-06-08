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

t = II()
for _ in range(t):
  n = II()
  s = list(SI())
  
  for i in range(n-1):
    if s[i] > s[i+1]:
      l = i
      while l < n-1 and s[l] >= s[l+1]:
        s[l],s[l+1] = s[l+1],s[l]
        l += 1
      break

  print(''.join(s))