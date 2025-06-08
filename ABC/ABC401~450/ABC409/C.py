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

n,l = MI()


p = [0]
D = LI()
for i in range(n-1):
  d = D[i]
  p.append((p[-1]+d)%l)
  
if l%3 != 0:
  print(0)
  exit()
d = collections.Counter(p)
ans = 0
for b in p:
  a = b-l//3
  c = b+l//3
  if 0 <= a <= l and 0 <= c <= l:
    ans += d[a]*d[c]

print(ans)