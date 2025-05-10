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

A = [['?' for _ in range(w+2)]]
for _ in range(h):
  A.append(['?']+list(SI())+['?'])
A.append(['?' for _ in range(w+2)])

objH = [[] for _ in range(h+2)]
objW = [[] for _ in range(w+2)]

for i in range(h+2):
  for j in range(w+2):
    if A[i][j] == "S":
      s = (i,j)
    elif A[i][j] == "G":
      g = (i,j)
    elif A[i][j] != '.':
      objH[i].append(j)
      objW[j].append(i)
    
  
que = collections.deque()
que.append(s)

dist = [[-1]*(w+2) for _ in range(h+2)]
dist[s[0]][s[1]] = 0

def canMove(x,y):
  if not (A[x][y] == '.' or A[x][y] == 'G'):
    return False

  leftobj = A[x][objH[x][bisect.bisect_right(objH[x], y)-1]]
  rightobj = A[x][objH[x][bisect.bisect_left(objH[x], y)]]
  if leftobj == '>' or rightobj == '<':
    return False
  
  upobj = A[objW[y][bisect.bisect_right(objW[y], x)-1]][y]
  downobj = A[objW[y][bisect.bisect_left(objW[y], x)]][y]
  
  if upobj == 'v' or downobj == '^':
    return False
  
  return True


while que:
  now = que.popleft()
  
  for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
    nx = now[0] + dx
    ny = now[1] + dy
    
    if dist[nx][ny] == -1 and canMove(nx,ny):
      dist[nx][ny] = dist[now[0]][now[1]] + 1
      que.append((nx,ny))

print(dist[g[0]][g[1]])