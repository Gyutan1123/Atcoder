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

n,m = MI()

AB = [LI() for _ in range(m)]

d = collections.defaultdict(int)

ans = 0
for i, (a,b) in enumerate(AB):
  a -= 1
  b -= 1
  if a > 0:
    b = (b+a)%n
  ans += i - d[b]
  d[b] += 1
  
print(ans)
