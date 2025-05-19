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

n,d = MI()
XY = [LI() for _ in range(n)]
XY.sort(key=lambda x: x[0])

que = []
ans = 0
i = 0

for t in range(1, d+1):
  while i < n and XY[i][0] == t:
    heapq.heappush(que, -XY[i][1])
    i += 1
  
  if len(que) > 0:
    ans += -heapq.heappop(que)
    
print(ans)
