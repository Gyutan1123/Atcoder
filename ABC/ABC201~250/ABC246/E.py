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

n = II()

A = tuple(MI())
B = tuple(LI())

S = ['#'*(n+2)]

for _ in range(n):
  s = '#'+SI()+'#'
  S.append(s)

S.append('#'*(n+2))

que = collections.deque()
dist = [[[float('inf')]*(4) for _ in range(n+1)] for _ in range(n+1)]
for i in range(4):
  que.append((A[0],A[1],i))
  dist[A[0]][A[1]][i] = 1

D = [(1,1),(1,-1),(-1,1),(-1,-1)]

while que:
  i,j,k = que.popleft()
  now_dist = dist[i][j][k]
  
  for d in range(4):
    if d == k:
      if S[i+D[d][0]][j+D[d][1]] == '.' and dist[i+D[d][0]][j+D[d][1]][d] > now_dist:
        que.appendleft((i+D[d][0],j+D[d][1],d))
        dist[i+D[d][0]][j+D[d][1]][d] = now_dist
    else:
      if S[i+D[d][0]][j+D[d][1]] == '.' and dist[i+D[d][0]][j+D[d][1]][d] > now_dist+1:
        que.append((i+D[d][0],j+D[d][1],d))
        dist[i+D[d][0]][j+D[d][1]][d] = now_dist+1
  
if min(dist[B[0]][B[1]]) != float('inf'):
  print(min(dist[B[0]][B[1]]))
else:
  print(-1)