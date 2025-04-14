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
C = [list(SI()) for _ in range(h)]

for i in range(h):
  for j in range(w):
    if C[i][j] == "S":
      si,sj = i,j
      
ans = 'No'
D = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(si,sj, goals):
  if not (0 <= si < h and 0 <= sj < w):
    return
  if C[si][sj] == "#":
    return
  
  visited = [[False]*(w) for _ in range(h)]
  que = collections.deque()
  que.append((si,sj))
  
  visited[si][sj] = True
  
  while que:
    i,j = que.popleft()
    for d in D:
      toi,toj = i+d[0],j+d[1]
      if 0 <= toi < h and 0 <= toj < w and C[toi][toj] == "." and visited[toi][toj] == False:
        visited[toi][toj] = True
        que.append((toi,toj))
        
  for gi,gj in goals:
    if not (0 <= gi < h and 0 <= gj < w):
      continue
    
    if visited[gi][gj] == True:
      global ans
      ans = "Yes"
      

bfs(si+1,sj,[(si-1,sj),(si,sj+1),(si,sj-1)])
bfs(si-1,sj,[(si+1,sj),(si,sj+1),(si,sj-1)])
bfs(si,sj-1,[(si-1,sj),(si+1,sj),(si,sj+1)])
bfs(si,sj+1,[(si-1,sj),(si+1,sj),(si,sj-1)])

print(ans)