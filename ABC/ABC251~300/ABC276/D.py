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

n = II()
a = LI()

p = []

mind2 = float('inf')
mind3 = float('inf')

for i in range(n):
  d2 = 0
  tmp = a[i]
  while tmp % 2 == 0:
    d2 += 1
    tmp //= 2
  mind2 = min(mind2,d2)  
  
  d3 = 0
  while tmp % 3 == 0:
    d3 += 1
    tmp //= 3  
  mind3 = min(mind3,d3)
  
  p.append((d2,d3))
  
ans = 0
for i in range(n):
  d2,d3 = p[i]
  if d2 > mind2:
    a[i] //= 2**(d2-mind2)
    ans += d2-mind2
  if d3 > mind3:
    a[i] //= 3**(d3-mind3)
    ans += d3-mind3

if len(set(a)) == 1:
  print(ans)
else:
  print(-1)