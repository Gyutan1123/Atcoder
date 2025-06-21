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

n,q = MI()
A = LI()

masu = [0]*(n+1)

ans = 0
for i in range(q):
  if n == 1:
    if masu[A[i]] == 0:
      ans += 1
      masu[A[i]] = 1
    else:
      ans -= 1
      masu[A[i]] = 0
    print(ans)
    continue
  
  if masu[A[i]] == 0:
    if A[i] == 1:
      if masu[A[i]+1] == 0:
        ans += 1
    elif A[i] == n:
      if masu[A[i]-1] == 0:
        ans += 1
    else:
      if masu[A[i]-1] == 0 and masu[A[i]+1] == 0:
        ans += 1
      elif masu[A[i]-1] == 1 and masu[A[i]+1] == 1:
        ans -= 1
    masu[A[i]] = 1
  
  else:
    if A[i] == 1:
      if masu[A[i]+1] == 0:
        ans -= 1
    elif A[i] == n:
      if masu[A[i]-1] == 0:
        ans -= 1
    else:
      if masu[A[i]-1] == 0 and masu[A[i]+1] == 0:
        ans -= 1
      elif masu[A[i]-1] == 1 and masu[A[i]+1] == 1:
        ans += 1
    masu[A[i]] = 0
  print(ans)
        