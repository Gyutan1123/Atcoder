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
dist = [-1]*(n+m+1)
connect = [[] for _ in range(n+m+1)]
for i in range(n):
  a = II()
  S = LI()
  for j in range(a):
    connect[m+1+i].append(S[j])
    connect[S[j]].append(m+1+i)
    
que = collections.deque()
que.append(1)
dist[1] = 0

while que:
  now = que.popleft()
  for to in connect[now]:
    if dist[to] == -1:
      dist[to] = dist[now]+1
      que.append(to)
      
if dist[m] != -1:
  print(dist[m]//2-1)
else:
  print(-1)