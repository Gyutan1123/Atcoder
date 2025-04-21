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

t = II()
for _ in range(t):
  n,m = MI()
  C = LI()
  connect = [[] for _ in range(n+1)]
  for _ in range(m):
    u,v = MI()
    connect[u].append(v)
    connect[v].append(u)
    
  que = collections.deque()
  que.append((1,n))
  
  dist = [[-1]*(n+1) for _ in range(n+1)]
  dist[1][n] = 0
  
  while que:
    T,A = que.popleft()
    for tot in connect[T]:
      for toa in connect[A]:
        if C[tot-1] != C[toa-1] and dist[tot][toa] == -1:
          dist[tot][toa] = dist[T][A]+1
          que.append((tot,toa))
  
  print(dist[n][1])