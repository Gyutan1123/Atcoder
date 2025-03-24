import sys
import collections, heapq, string, math, itertools

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(LS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

h,w = MI()
ans = -1
C = [list(SI()) for _ in range(h)]

D = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(now, visited, k, station):
  for d in D:
    c_to = now[0]+d[0]
    r_to = now[1]+d[1]
    if ((0 <= c_to and c_to < h)
        and (0 <= r_to and r_to < w)
        and visited[c_to][r_to] == False 
        and C[c_to][r_to] == '.'):
      
      if (c_to, r_to) == station and k >= 2:
        global ans
        ans = max(k+1, ans)
      
      if (c_to, r_to) != station:
        visited[c_to][r_to] = True
        dfs((c_to,r_to),visited,k+1,station)
        visited[c_to][r_to] = False
        

for i in range(h):
  for j in range(w):
    visited = [[False]*(w) for _ in range(h)]
    if C[i][j] == '.':
      dfs((i,j),visited,0,(i,j))
      
print(ans)