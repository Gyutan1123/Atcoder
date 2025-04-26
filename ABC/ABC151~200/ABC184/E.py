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

h,w = MI()


connect = collections.defaultdict(list)
A = []

for i in range(h):
  a = SI()
  for j in range(w):
    if a[j] == 'S':
      s = (i,j)
    if a[j] == 'G':
      g = (i,j)
    if 'a' <= a[j] <= 'z':
      connect[a[j]].append((i,j)) 
  A.append(a)
      
D = [(1,0),(-1,0),(0,1),(0,-1)] 
hdist = collections.defaultdict(lambda:-1)
dist = [[-1]*w for _ in range(h)] 
que = collections.deque()
que.append(s)
dist[s[0]][s[1]] = 0

while que:
  now = que.popleft()
  if len(now) == 1:
    for to in connect[now]:
      i,j = to
      if dist[i][j] == -1 or dist[i][j] > hdist[now]+1:
        dist[i][j] = hdist[now]+1
        que.append(to)
  else:
    i,j = now
    if'a' <= A[i][j] <= 'z':
      if hdist[A[i][j]] == -1 or hdist[A[i][j]] > dist[i][j]:
        hdist[A[i][j]] = dist[i][j]
        que.appendleft(A[i][j])
    for d in D:
      toi,toj = now[0]+d[0],now[1]+d[1]
      if (0 <= toi < h and 0 <= toj < w 
          and A[toi][toj] != '#' 
          and (dist[toi][toj] == -1 or dist[toi][toj] > dist[i][j]+1)):
        dist[toi][toj] = dist[i][j]+1
        que.append((toi,toj))
        
print(dist[g[0]][g[1]])