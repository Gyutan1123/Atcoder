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

def dijkstra(graph, start, getPath=False, goal=None):
  """
  Args:
      graph : 隣接リスト(頂点と重みのタプル)
      start : 開始位置
      getPath : 経路復元するかどうか
      goal : 経路復元する場合の目的地
      
  Returns: startからの最短距離を格納したリスト
           (と、goalまでの最短経路に含まれる各頂点を格納したリスト
           経路が存在しない場合は空のリスト)
  """
  n = len(graph)
  visited = [False]*n
  dist = [float('inf')]*n
  dist[start] = 0
  
  if getPath:
    prev = [-1] * n
    shortestPath = []
    
  # (距離、番号)をheapに入れていく
  que = []
  heapq.heappush(que,(0, start))
  while que:
    _,now = heapq.heappop(que)
    
    if visited[now]:
      continue
    
    visited[now] = True
    for to, cost in graph[now]:
      if dist[to] > dist[now] + cost :
        dist[to] = dist[now] + cost
        heapq.heappush(que,(dist[to], to))
        if getPath:
          prev[to] = now
          
    if getPath and visited[goal]:
      now = goal
      shortestPath.append(goal)
      while now != start:
        now = prev[now]
        shortestPath.append(now)
      
  if getPath:
    return dist, shortestPath
  else:
    return dist

n,m = MI()
H = LI()

connect = [[] for _ in range(n+1)]

for i in range(m):
  u,v = MI()
  hu,hv = H[u-1],H[v-1]
  if hu >= hv:
    connect[u].append((v,0)) 
    connect[v].append((u, hu-hv))
  else:
    connect[v].append((u,0)) 
    connect[u].append((v, hv-hu))
  
dist = dijkstra(connect, 1)

ans = 0
hs = H[0]
for i in range(n):
  hg = H[i]
  ans = min(ans,dist[i+1]+hg-hs)

print(-ans)