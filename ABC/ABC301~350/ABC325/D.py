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

TD = [LI() for _ in range(n)]
TE = [(t,t+d) for t,d in TD]
TE.sort(key=lambda x: x[0])

ans = 0
lastTime = 0

que = []
now = 0
while True:
  if len(que) == 0:
    if now == n:
      break
    i = TE[now][0]
    
  while now < n and TE[now][0] == i:
    heapq.heappush(que, TE[now][1])
    now += 1
  
  while len(que) > 0 and que[0] < i:
    heapq.heappop(que)
  
  if que:
    heapq.heappop(que)
    ans += 1
  
  i += 1
    
print(ans)
