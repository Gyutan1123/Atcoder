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
connectI = [[] for _ in range(n+1)]
g = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
  u,v = MI()
  connect[u].append(v)
  g[u][v] = True
  
que = collections.deque()

ans = 0

for i in range(1,n+1):
  que.append(i)
  dist = [-1]*(n+1)
  dist[i] = 0

  while que:
    now = que.popleft()
    for to in connect[now]:
      if dist[to] == -1:
        dist[to] = dist[now]+1
        que.append(to)
        if g[i][to] == False:
          ans += 1

print(ans)