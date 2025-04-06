import sys
import collections, heapq, string, math, itertools, copy
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
S = []

for i in range(h):
  s = SI()
  S.append(s)
  

A,B,C,D = MI()
dist = [[float('inf')]*(w) for _ in range(h)]
dist[A-1][B-1] = 0
que = collections.deque()
que.append((A-1,B-1))

D1 = [(1,0),(-1,0),(0,1),(0,-1)]
D2 = [(2,0),(-2,0),(0,2),(0,-2)]
while que:
  now = que.popleft()
  i,j = now
  now_dist = dist[i][j]
  
  for d in D1:
    if 0 <= i+d[0] < h and 0 <= j+d[1] < w and S[i+d[0]][j+d[1]] == '.' and now_dist < dist[i+d[0]][j+d[1]]:
      dist[i+d[0]][j+d[1]] = now_dist
      que.appendleft((i+d[0],j+d[1]))
    
    if 0 <= i+d[0] < h and 0 <= j+d[1] < w and S[i+d[0]][j+d[1]] == '#' and now_dist+1 < dist[i+d[0]][j+d[1]]:
      dist[i+d[0]][j+d[1]] = now_dist+1
      que.append((i+d[0],j+d[1]))
      
  for d in D2:
    if 0 <= i+d[0] < h and 0 <= j+d[1] < w and now_dist+1 < dist[i+d[0]][j+d[1]] and S[i+d[0]][j+d[1]] != '?':
      dist[i+d[0]][j+d[1]] = now_dist+1
      que.append((i+d[0],j+d[1]))

print(dist[C-1][D-1])