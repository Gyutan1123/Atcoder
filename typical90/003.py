import sys
from collections import deque

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################


n = II()
connect = [[] for _ in range(n+1)]

for _ in range(n-1):
  a,b = MI()
  connect[a].append(b)
  connect[b].append(a)
  
que = deque()

que.append(1)

dist = [0]*(n+1)
visited = [False]*(n+1)
visited[1] = True

while que:
  now = que.popleft()
  for to in connect[now]:
    if visited[to] == False:
      que.append(to)
      visited[to] = True
      dist[to] = dist[now] + 1
      
# 直径の端点
u = dist.index(max(dist))

que.append(u)

dist = [0]*(n+1)
visited = [False]*(n+1)
visited[u] = True

while que:
  now = que.popleft()
  for to in connect[now]:
    if visited[to] == False:
      que.append(to)
      visited[to] = True
      dist[to] = dist[now] + 1
      
print(1+max(dist))