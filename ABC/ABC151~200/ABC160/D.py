import sys
import collections, heapq, string
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

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
n,x,y = MI()

connection = [[] for _ in range(n+1)]

for i in range(1,n):
  connection[i].append((i+1,1))
  connection[i+1].append((i,1))
  
connection[x].append((y,1))
connection[y].append((x,1))

ans = [0]*(n)

for i in range(1,n+1):
  dist = dijkstra(connection,i)
  for j in range(i+1, n+1):
    ans[dist[j]] += 1
    
for k in range(1,n):
  print(ans[k])
    

