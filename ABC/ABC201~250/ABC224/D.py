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

m = II()
connect = [[] for _ in range(10)]
for _ in range(m):
  u,v = MI()
  connect[u].append(v)
  connect[v].append(u)
p = tuple(MI())

que = collections.deque()
que.append(p)
visited = collections.defaultdict(lambda:False)
visited[p] = True
dist = collections.defaultdict(lambda:0)

while que:
  now = que.popleft()
  now_dist = dist[now]
  # 空白マス
  for i in range(1,10):
    if i not in now:
      free = i
  
  # to : 次に空白になるマス
  for to in connect[free]:
    tmp = list(now)
    # tmp.index(to): そのマスに置かれているコマのindex
    tmp[tmp.index(to)] = free
    tmp = tuple(tmp)
    if visited[tmp] == False:
      visited[tmp] = True
      que.append(tmp)
      dist[tmp] = now_dist+1
      
ans = tuple(range(1,9))
if visited[ans]:
  print(dist[ans])
else:
  print(-1)