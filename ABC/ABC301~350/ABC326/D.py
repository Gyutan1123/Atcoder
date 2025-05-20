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

n = II()
R = SI()
C = SI()

def check(grid):
  
  for i in range(n):
    num = [0, 0, 0]
    for j in range(n):
      if grid[i][j] == 'A':
        num[0] += 1
      elif grid[i][j] == 'B':
        num[1] += 1
      elif grid[i][j] == 'C':
        num[2] += 1
    if not(num[0] == 1 and num[1] == 1 and num[2] == 1):
      return False
  
  for j in range(n):
    num = [0, 0, 0]
    for i in range(n):
      if grid[i][j] == 'A':
        num[0] += 1
      elif grid[i][j] == 'B':
        num[1] += 1
      elif grid[i][j] == 'C':
        num[2] += 1
    if not(num[0] == 1 and num[1] == 1 and num[2] == 1):
      return False
  
  for i in range(n):
    for j in range(n):
      if grid[i][j] != '.':
        if grid[i][j] != R[i]:
          return False
        break
  for j in range(n):
    for i in range(n):
      if grid[i][j] != '.':
        if grid[i][j] != C[j]:
          return False
        break
  
  return True


def dfs(nowGrid, Aavail, Bavail, Cavail, decideNum):
  global n
  global ans
  global flag
  
  if decideNum == 3*n:

    if check(nowGrid):    
      ans = nowGrid
      flag = True
  else:
    r = decideNum // 3
    s = decideNum % 3
    
    if s == 0:
      if len(Aavail) == 0:
        return False
      for j in Aavail:
        if nowGrid[r][j] != '.':
          continue
        nextGrid = copy.deepcopy(nowGrid)
        nextGrid[r][j] = 'A'
        nextAavail = Aavail.copy()
        nextAavail.remove(j)
        dfs(nextGrid, nextAavail, Bavail, Cavail, decideNum+1)
    elif s == 1:
      if len(Bavail) == 0:
        return False
      for j in Bavail:
        if nowGrid[r][j] != '.':
          continue
        nextGrid = copy.deepcopy(nowGrid)
        nextGrid[r][j] = 'B'
        nextBavail = Bavail.copy()
        nextBavail.remove(j)
        dfs(nextGrid, Aavail, nextBavail, Cavail, decideNum+1)
    elif s == 2:
      if len(Cavail) == 0:
        return False
      for j in Cavail:
        if nowGrid[r][j] != '.':
          continue
        nextGrid = copy.deepcopy(nowGrid)
        nextGrid[r][j] = 'C'
        nextCavail = Cavail.copy()
        nextCavail.remove(j)
        
        dfs(nextGrid, Aavail, Bavail, nextCavail, decideNum+1)
  
ans = []
flag = False

dfs([['.']*n for _ in range(n)], [i for i in range(n)], [i for i in range(n)], [i for i in range(n)], 0)
if flag:
  print('Yes')
  for i in range(n):
    print(''.join(ans[i]))
else:
  print('No')