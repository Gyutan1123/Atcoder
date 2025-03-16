import sys
import collections, heapq, string, math
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

mod = 10**9 + 7
########################################################

n = II()
connect = [[] for _ in range(n+1)]

for i in range(n-1):
  a,b = MI()
  connect[a].append(b)
  connect[b].append(a)
  
que = collections.deque()
dist = [-1]*(n+1)

que.append(1)
dist[1] = 0

ans1 = [1]
ans2 = []

while que:
  now = que.popleft()
  
  for to in connect[now]:
    if dist[to] != -1:
      continue
    
    dist[to] = dist[now] + 1
    que.append(to)
    if dist[to] % 2 == 0:
      ans1.append(to)
    else:
      ans2.append(to)
      
  
if len(ans1) >= n // 2:
  print(*ans1[:n//2])
else:
  print(*ans2[:n//2])
  
  