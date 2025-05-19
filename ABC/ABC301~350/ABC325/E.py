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
import heapq
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


n,a,b,c = MI()

D = [LI() for _ in range(n)]

graph = [[] for _ in range(2*n)]
for i in range(n):
  graph[i].append((i+n, 0))
  for j in range(n):
    d = D[i][j]
    graph[i].append((j,d*a))
    graph[i+n].append((j+n,d*b+c))

dist = dijkstra(graph, 0)
print(min(dist[n-1],dist[2*n-1]))