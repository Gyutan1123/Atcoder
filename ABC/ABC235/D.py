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

a,n = MI()
l = len(str(n))

visited = collections.defaultdict(lambda:False)
dist = collections.defaultdict(lambda:-1)
visited[1] = True
dist[1] = 0

que = collections.deque()
que.append(1)

while que:
  now = que.popleft()
  now_dist = dist[now]
  if now > 10 and now%10 != 0:
    tmp = now
    L = len(str(tmp))
    tmpl = ['']*(L)
    for i in range(L):
      tmpl[L-1-i] = str(tmp%10)
      tmp //= 10
    to = int(''.join(tmpl[-1:]+tmpl[:-1]))
    if to < 10**6 and visited[to] == False:
      visited[to] = True
      dist[to] = now_dist+1
      que.append(to)
  
  to = a*now
  if to < 10**6 and visited[to] == False:
    visited[to] = True
    dist[to] = now_dist+1
    que.append(to)

print(dist[n])