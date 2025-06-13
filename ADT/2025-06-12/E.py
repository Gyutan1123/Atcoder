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
d = dict()
ans = 0
def dfs(n):
  if n in d:
    return d[n]
  
  if n <= 1: 
    return 0
  else:
    tmp = n
    tmp += dfs(n//2)
    tmp += dfs((n+1)//2)
    d[n] = tmp
    return tmp
  
print(dfs(n))