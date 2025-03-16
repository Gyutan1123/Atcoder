import sys
import collections, heapq, string, math
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

mod = 10**9 + 7
########################################################

n = II()

grid = [[0]*1001 for _ in range(1001)]

for _ in range(n):
  lx,ly,rx,ry = MI()
  grid[lx][ly] += 1
  grid[lx][ry] -= 1
  grid[rx][ly] -= 1
  grid[rx][ry] += 1

for i in range(1000):
  for j in range(1000):
    grid[i][j+1] += grid[i][j]
    
for j in range(1000):
  for i in range(1000):
    grid[i+1][j] += grid[i][j]
    
ans = [0]*(n+1)

for i in range(1000):
  for j in range(1000):
    ans[grid[i][j]] += 1
    
      
for i in range(1,n+1):
  print(ans[i])