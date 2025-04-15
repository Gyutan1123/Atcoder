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

n,m = MI()
a = LI()
a.sort()
s = sum(a)

a += a

ans = float("inf")
i = 0
while i < 2*n:
  tmp = a[i]
  j = i+1
  cnt = 1
  while j < 2*n and (a[j-1] == a[j] or (a[j-1]+1)%m == a[j]) and cnt < n:
    tmp += a[j]
    j += 1
    cnt += 1
  
  ans = min(ans,s-tmp)
  
  i = j


print(ans)