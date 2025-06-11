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

p = [True]*(2*10**6+2)
p[0] = False
p[1] = False


for i in range(2,2*10**6+2):
  if p[i]:
    for j in range(i*2, 2*10**6+2, i):
      p[j] = False
    

P = [i for i in range(2*10**6+2) if p[i]]


ans = 0
for i in range(len(P)):
  p = P[i]
  l = i
  r = len(P)
  while r-l > 1:
    mid = (l+r)//2
    q = P[mid]
    if pow(p*q,2) <= n:
      l = mid
    else:
      r = mid

  ans += l-i 
  
for p in P:
  if pow(p,8) <= n:
    ans += 1

print(ans)
