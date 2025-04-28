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

n,m,k = MI()
connect = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = MI()
  connect[u].append(v)
  connect[v].append(u)
  
H = [-1]*(n+1)
visited = [False]*(n+1)
que = []

for _ in range(k):
  p,h = MI()
  H[p] = h

for i in range(1,n+1):
  heapq.heappush(que, (-H[i], i))
  
while que:
  _,p = heapq.heappop(que)
  if visited[p]:
    continue
  visited[p] = True
  for to in connect[p]:
    if H[to] < H[p]-1:
      H[to] = H[p]-1
      heapq.heappush(que, (-H[to], to))
      
ans = []
for i in range(1,n+1):
  if H[i] >= 0:
    ans.append(i)
  
print(len(ans))
print(*ans)