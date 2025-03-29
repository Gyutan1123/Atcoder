import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

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
heap = []
Next = [set() for _ in range(n+1)]
Prev = [set() for _ in range(n+1)]

queSet = set()
for _ in range(m):
  a,b = MI()
  Next[a].add(b)
  Prev[b].add(a)
  
for i in range(1,n+1):
  if len(Prev[i]) == 0:
    heapq.heappush(heap,i)
    queSet.add(i)
    
ans = []

while heap:
  now = heapq.heappop(heap)
  ans.append(now)
  for a in Next[now]:
    Prev[a].remove(now)
    if len(Prev[a]) == 0:
      heapq.heappush(heap, a)


if len(ans) == n:
  print(*ans)
else:
  print(-1)