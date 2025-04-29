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

n1,n2,m = MI()

graph = [[] for _ in range(n1+n2+1)]
for _ in range(m):
  a,b = MI()
  graph[a].append(b)
  graph[b].append(a)

dist1 = [-1]*(n1+n2+1)
dist2 = [-1]*(n1+n2+1)


que = collections.deque()
que.append(1)
dist1[1] = 0

while que:
  now = que.popleft()
  for to in graph[now]:
    if dist1[to] == -1:
      dist1[to] = dist1[now] + 1
      que.append(to)
  
dmax1 = 0
for i in range(1,n1+1):
  dmax1 = max(dmax1, dist1[i])

que.append(n1+n2)
dist2[n1+n2] = 0
while que:
  now = que.popleft()
  for to in graph[now]:
    if dist2[to] == -1:
      dist2[to] = dist2[now] + 1
      que.append(to)
dmax2 = 0
for i in range(n1+1,n1+n2+1):
  dmax2 = max(dmax2, dist2[i])

print(dmax1+dmax2+1)