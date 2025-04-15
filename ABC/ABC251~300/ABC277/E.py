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
  u,v,a = MI()
  connect[u].append((v,a))
  connect[v].append((u,a))
  
S = set(LI())

dist = [[float('inf')]*2 for _ in range(n+1)]
dist[1][1] = 0

que = collections.deque()
que.append((1,1))

while que:
  now, s = que.popleft()
  
  if now in S:
    if dist[now][(s+1)%2] > dist[now][s]:
      dist[now][(s+1)%2] = dist[now][s]
      que.appendleft((now,(s+1)%2))
      
  for to, a in connect[now]:
    if a != s:
      continue
    
    if dist[to][s] > dist[now][s] + 1:
      dist[to][s] = dist[now][s]+1
      que.append((to,s))

if min(dist[n]) != float('inf'):
  print(min(dist[n]))
else:
  print(-1)