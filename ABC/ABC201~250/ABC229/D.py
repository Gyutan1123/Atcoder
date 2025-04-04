import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

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
k = II()
n = len(s)
l = 0
r = n+1

accum = [0]*(n+1)
for i in range(n):
  if s[i] == '.':
    accum[i+1] += 1
for i in range(n):
  accum[i+1] += accum[i]

while r-l > 1:
  mid = (r+l)//2
  flag = False
  for i in range(n-mid+1):
    if accum[i+mid] - accum[i] <= k:
      flag = True
  if flag:
    l = mid
  else:
    r = mid

print(l)