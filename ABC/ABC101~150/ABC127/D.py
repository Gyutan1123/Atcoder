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
A = LI()
A.sort()
BC = [LI() for _ in range(m)]

que = []
for a in A:
  heapq.heappush(que, (-a,1))

for b,c in BC:
  heapq.heappush(que, (-c,b))
  
ans = 0
for i in range(n):
  a,c = heapq.heappop(que)
  ans += -a
  if c > 1:
    heapq.heappush(que, (a,c-1))

print(ans)