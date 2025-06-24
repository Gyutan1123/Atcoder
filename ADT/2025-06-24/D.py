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
connect = [[] for _ in range(n)]
for _ in range(n-1):
  a,b = MI()
  connect[a-1].append(b-1)
  connect[b-1].append(a-1)

cnt1 = 0
cnt2 = 0
for i in range(n):
  if len(connect[i]) == n-1:
    cnt1 += 1
  if len(connect[i]) == 1:
    cnt2 += 1

if cnt1 == 1 and cnt2 == n-1:
  print("Yes")
else:
  print("No")
