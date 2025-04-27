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

n = II()
connect = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = MI()
    connect[a].append(b)
    connect[b].append(a)
    
g = [-1]*(n+1)
s = 0
for i in range(1, n+1):
  if len(connect[i]) == 1:
    s = i
    break

g[s] = 0
que = collections.deque([s])
while que:
  now = que.popleft()
  nowg = g[now]
  if nowg == 1:
    for to in connect[now]:
      if g[to] == -1:
        g[to] = 0
        que.append(to)
  elif nowg == 0:
    if len(connect[now]) == 1:
      for to in connect[now]:
        if g[to] == -1:
          g[to] = 1
          que.append(to)
    else:
      a = connect[now][0]
      b = connect[now][1]
      if g[a] == -1 and g[b] == 1:
        g[a] = 0
        que.append(a)
      elif g[a] == -1 and g[b] == 0:
        g[a] = 1
        que.append(a)
      elif g[a] == 1 and g[b] == -1:
        g[b] = 0
        que.append(b)
      elif g[a] == 0 and g[b] == -1:
        g[b] = 1
        que.append(b)

L = []
for i in range(1, n+1):
  if g[i] == 1:
    L.append(len(connect[i]))

L.sort()
print(*L)