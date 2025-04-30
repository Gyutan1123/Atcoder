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
P = LI()
P.sort()
L = LI()
D = LI()

V = [(L[i], D[i]) for i in range(m)]
V.sort()

que = []

ans = sum(P)

j = 0
k = -1
for i in range(n):
  for k in range(j, bisect.bisect_right(V, (P[i], float('inf')))):
    heapq.heappush(que, -V[k][1])
  j = k+1

  if len(que) > 0:
    ans += heapq.heappop(que)

print(ans)