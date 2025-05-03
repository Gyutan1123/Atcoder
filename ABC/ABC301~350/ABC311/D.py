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

n,m = MI()
S = [SI() for _ in range(n)]

rr = [[] for _ in range(n)]
rc = [[] for _ in range(m)]

for i in range(n):
  for j in range(m):
    if S[i][j] == '#':
      rr[i].append(j)
      rc[j].append(i)
      
que = collections.deque()
que.append((1,1))

stoped = [[False]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
visited[1][1] = True
stoped[1][1] = True
while que:
  i,j = que.popleft()
  
  toj = rr[i][bisect.bisect_left(rr[i],j)-1]+1
  for k in range(toj,j+1):
    visited[i][k] = True
  if not stoped[i][toj]:
    stoped[i][toj] = True
    que.append((i,toj))
    
  toj = rr[i][bisect.bisect_right(rr[i],j)]-1
  for k in range(j, toj+1):
    visited[i][k] = True
  if not stoped[i][toj]:
    stoped[i][toj] = True
    que.append((i,toj))
    
  toi = rc[j][bisect.bisect_left(rc[j],i)-1]+1
  for k in range(toi,i+1):
    visited[k][j] = True
  if not stoped[toi][j]:
    stoped[toi][j] = True
    que.append((toi,j))
  
  toi = rc[j][bisect.bisect_right(rc[j],i)]-1
  for k in range(i, toi+1):
    visited[k][j] = True
  if not stoped[toi][j]:
    stoped[toi][j] = True
    que.append((toi,j))
    

ans = 0
for i in range(n):
  for j in range(m):
    if visited[i][j]:
      ans += 1

print(ans)