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

s = SI()
q = II()
K = LI()


def dfs(k, l):
  if l == 0:
    return s[k-1]
  
  h = len(s)<<(l-1)
  
  if k <= h:
    return dfs(k,l-1)
  else:
    return dfs(k-h,l-1).swapcase()
  

ans = []
for k in K:
  ans.append(dfs(k, 100))
  
print(*ans)