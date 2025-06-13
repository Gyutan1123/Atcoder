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
A.sort()
s = [0]
for i in range(n):
  s.append(s[-1]+A[i])
  
ans = 0
for i in range(n-1):
  ans += s[n]-s[i+1]
  ans += A[i]*(n-i-1)
  
  l = i
  r = n
  while r-l > 1:
    mid = (l+r)//2
    if A[mid]+A[i] >= 10**8:
      r = mid
    else:
      l = mid
  ans -= 10**8*(n-r)
  
print(ans)
