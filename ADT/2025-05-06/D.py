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

num = [0]*(n)
d = [[] for _ in range(37)]

for i in range(n):
  c = II()
  A = LI()
  num[i] = c
  for a in A:
    d[a].append(i)
    
x = II()

m = float('inf')
for i in d[x]:
  m = min(m,num[i])

ans = []
for i in d[x]:
  if num[i] == m:
    ans.append(i+1)
ans.sort()
print(len(ans))
print(*ans)