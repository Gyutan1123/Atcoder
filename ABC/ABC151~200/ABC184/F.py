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

n,t = MI()
A = LI()

A1 = A[:n//2]
A2 = A[n//2:]

T1 = [0]
for i in range(1<<len(A1)):
  s = 0
  for j in range(len(A1)):
    if i & (1<<j):
      s += A1[j]
  if s <= t:
    T1.append(s)
T1.sort()

T2 = [0]
for i in range(1<<len(A2)):
  s = 0
  for j in range(len(A2)):
    if i & (1<<j):
      s += A2[j]
  if s <= t:
    T2.append(s)
T2.sort()

ans = 0


for t1 in T1:
  l = 0
  r = len(T2)
  
  while r-l > 1:
    mid = (l+r)//2
    if t1 + T2[mid] <= t:
      l = mid
    else:
      r = mid
  
  ans = max(ans,t1+T2[l])

print(ans)