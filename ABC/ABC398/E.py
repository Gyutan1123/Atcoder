import sys
import collections, heapq, string, math, itertools

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(LS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n = II()
d = collections.defaultdict(set)

connect = [[] for _ in range(n+1)]

for _ in range(n-1):
  u,v = MI()
  d[u].add(v)
  d[v].add(u)
  connect[u].append(v)
  connect[v].append(u)
  

que = collections.deque()
que.append(1)
color = [0]*(n+1)
visited = [False]*(n+1)
visited[1] = True

while que:
  now = que.popleft()
  now_color = color[now]
  for to in connect[now]:
    if visited[to] == False:
      visited[to] = True
      que.append(to)
      color[to] = (now_color+1)%2
      
tehuda = set()

for i in range(1,n+1):
  for j in range(i+1, n+1):
    if (not i in d[j]) and color[i] != color[j]:
      tehuda.add((i,j))


if len(tehuda)%2 == 1:
  print('First',flush=True)
  p = tehuda.pop()
  print(p[0],p[1])
else:
  print('Second',flush=True)

while True:
  i,j =  MI()
  if i == -1 and j == -1:
    sys.exit()
    
  if i > j:
    i,j = j,i
  tehuda.remove((i,j))
  
  if len(tehuda) > 0:
    p = tehuda.pop()
    print(p[0],p[1],flush=True)
  else:
    print(-1,-1,flush=True)