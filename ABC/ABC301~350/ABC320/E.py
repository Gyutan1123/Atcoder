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
ret = []

ans = [0]*n
inrow = [i for i in range(n)]
heapq.heapify(inrow)
for i in range(m):
  t,w,s = MI()
  while ret and ret[0][0] <= t:
    _,top = heapq.heappop(ret)
    heapq.heappush(inrow,top)
  if inrow:
    top = heapq.heappop(inrow)
    ans[top] += w
    heapq.heappush(ret, (t+s,top))

for i in range(n):
  print(ans[i])