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

t = II()
for _ in range(t):
  n = II()
  s = SI()
  
  l = 0
  flag = False
  for i in range(n-1):
    if s[i] > s[i+1]:
      l = i
      start = s[i]
      flag = True
      break
  if not flag:
    print(s)  
    continue
  for r in range(l,n):
    if s[r] > start:
      break


  if r == n-1 and s[n-1] <= start:
    r = n 

  if l > 0:
    s1 = s[:l]
  else:
    s1 = ''
  s2 = s[l:r]
  s2shift = s2[1:]+s2[0]
  if r <= n-1:
    s3 = s[r:]
  else:
    s3 = ''
  ans = s1 + s2shift + s3

  print(ans)