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
S = [list(SI()) for _ in range(h)]

dist = [[-1]*w for _ in range(h)]

k1 = None
for i in range(h):
  for j in range(w):
    if S[i][j] == "o":
      if k1 is None:
        k1 = (i,j)
      else:
        k2 = (i,j)
        break

dist[k1[0]][k1[1]] = 0
q = collections.deque()
q.append(k1)
while q:
  x,y = q.popleft()
  for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
    nx,ny = x+dx,y+dy
    if 0 <= nx < h and 0 <= ny < w and dist[nx][ny] == -1:
      dist[nx][ny] = dist[x][y]+1
      q.append((nx,ny))

print(dist[k2[0]][k2[1]])
