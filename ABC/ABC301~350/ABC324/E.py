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

n,t = MS()
n = int(n)
L = []
R = []

for i in range(n):
  s = SI()
  iter = 0
  for j in range(len(s)):
    if s[j] == t[iter]:
      iter += 1
    if iter == len(t):
      break
  L.append(iter)
  
  iter = len(t)-1
  for j in reversed(range(len(s))):
    if s[j] == t[iter]:
      iter -= 1
    if iter == -1:
      break
  R.append((len(t)-1)-iter)
  
m = len(t)

ans = 0
R.sort()

for i in range(n):
  l = L[i]
  ans += n-bisect.bisect_left(R,m-l)
print(ans)