import sys
import collections, heapq, string, math, itertools, copy, bisect, functools
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
S = [SI() for _ in range(h)]

dist = [[float('inf')]*w for _ in range(h)]
ans = [[] for _ in range(h)]
for i in range(h):
  for s in S[i]:
    ans[i].append(s)
  

que = []
for i in range(h):
  for j in range(w):
    if S[i][j] == "E":
      que.append((i,j))
      dist[i][j] = 0
      
arrow = ['<','^','>','v']

que = collections.deque(que)
while que:
  x,y = que.popleft()
  d = dist[x][y]
  for i, (dx,dy) in enumerate([(0,1),(1,0),(0,-1),(-1,0)]):
    nx,ny = x+dx,y+dy
    if 0 <= nx < h and 0 <= ny < w and S[nx][ny] == ".":
      if dist[nx][ny] > d+1:
        dist[nx][ny] = d+1
        ans[nx][ny] = arrow[i]
        que.append((nx,ny))

for s in ans:
  print("".join(s))