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
A = LI()

d = [[] for _ in range(n+1)]
for i in range(n):
  d[A[i]].append(i)
  
ans = 0
for i in range(1,n+1):
  l = 0
  for j in d[i]:
    ans += (j-l+1)*(n-j)
    l = j+1
print(ans)