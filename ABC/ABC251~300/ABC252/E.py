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

connect = [[] for _ in range(n+1)]
for i in range(m):
  a,b,c = MI()
  connect[a].append((b,c,i+1))
  connect[b].append((a,c,i+1))
  
visited = [False]*(n+1)
dist = [float('inf')]*(n+1)
dist[1] = 0

que = []
prev = [-1]*(n+1)

heapq.heappush(que,(0,1))
while que:
  _,now = heapq.heappop(que)
  
  if visited[now]:
    continue
  
  visited[now] = True
  for to, cost, id in connect[now]:
    if dist[to] > dist[now]+cost:
      dist[to] = dist[now]+cost
      heapq.heappush(que,(dist[to], to))
      prev[to] = id
  
for i in range(2,n+1):
  print(prev[i])