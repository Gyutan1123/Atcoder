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

connect = [[] for _ in range(n+m+1)]
for i in range(m):
  k = II()
  R = LI()
  for j in range(k):
    connect[n+1+i].append(R[j])
    connect[R[j]].append(n+1+i)
    
que = collections.deque()
que.append(1)
dist = [-1]*(n+m+1)
dist[1] = 0

while que:
  now = que.popleft()
  for to in connect[now]:
    if dist[to] == -1:
      dist[to] = dist[now]+1
      que.append(to)
      
for i in range(1,n+1):
  d = dist[i]
  print(d//2)