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
graph = [[False]*n for _ in range(n)]
for _ in range(m):
  a,b = MI()
  graph[a-1][b-1] = True
  graph[b-1][a-1] = True

ans = float('inf')
for p in itertools.permutations(range(n)):
  cnt = 0
  checked = set()
  for i in range(n-1):
    if not graph[p[i]][p[i+1]]:
      cnt += 1
    checked.add((min(p[i], p[i+1]), max(p[i], p[i+1])))
  if not graph[p[-1]][p[0]]:
    cnt += 1
  checked.add((min(p[-1], p[0]), max(p[-1], p[0])))
 
  for i in range(n):
    for j in range(i+1,n):
      if (i,j) in checked or (j,i) in checked:
        continue
      if graph[i][j]:
        cnt += 1
  
  ans = min(ans, cnt)
  
  if n == 6:
    cnt = 0
    checked = set()
    if not graph[p[0]][p[1]]:
      cnt += 1
    checked.add((min(p[0], p[1]), max(p[0], p[1])))
    if not graph[p[1]][p[2]]:
      cnt += 1
    checked.add((min(p[1], p[2]), max(p[1], p[2])))
    if not graph[p[2]][p[0]]:
      cnt += 1
    checked.add((min(p[2], p[0]), max(p[2], p[0])))
    
    if not graph[p[3]][p[4]]:
      cnt += 1
    checked.add((min(p[3], p[4]), max(p[3], p[4])))
    if not graph[p[4]][p[5]]:
      cnt += 1
    checked.add((min(p[4], p[5]), max(p[4], p[5])))
    if not graph[p[5]][p[3]]:
      cnt += 1
    checked.add((min(p[5], p[3]), max(p[5], p[3])))
    
    for i in range(n):
      for j in range(i+1,n):
        if (i,j) in checked or (j,i) in checked:
          continue
        if graph[i][j]:
          cnt += 1

    ans = min(ans, cnt)
   
  if n == 7:
    cnt = 0
    checked = set()
    if not graph[p[0]][p[1]]:
      cnt += 1
    checked.add((min(p[0], p[1]), max(p[0], p[1])))
    if not graph[p[1]][p[2]]:
      cnt += 1
    checked.add((min(p[1], p[2]), max(p[1], p[2])))
    if not graph[p[2]][p[3]]:
      cnt += 1
    checked.add((min(p[2], p[3]), max(p[2], p[3])))
    if not graph[p[3]][p[0]]:
      cnt += 1
    checked.add((min(p[3], p[0]), max(p[3], p[0])))
    
    if not graph[p[4]][p[5]]:
      cnt += 1
    checked.add((min(p[4], p[5]), max(p[4], p[5])))
    if not graph[p[5]][p[6]]:
      cnt += 1
    checked.add((min(p[5], p[6]), max(p[5], p[6])))
    if not graph[p[6]][p[4]]:
      cnt += 1
    checked.add((min(p[6], p[4]), max(p[6], p[4])))
    
    for i in range(n):
      for j in range(i+1,n):
        if (i,j) in checked or (j,i) in checked:
          continue
        if graph[i][j]:
          cnt += 1

    ans = min(ans, cnt)
  
  if n == 8:
    cnt = 0
    checked = set()
    if not graph[p[0]][p[1]]:
      cnt += 1
    checked.add((min(p[0], p[1]), max(p[0], p[1])))
    if not graph[p[1]][p[2]]:
      cnt += 1
    checked.add((min(p[1], p[2]), max(p[1], p[2])))
    if not graph[p[2]][p[3]]:
      cnt += 1
    checked.add((min(p[2], p[3]), max(p[2], p[3])))
    if not graph[p[3]][p[0]]:
      cnt += 1
    checked.add((min(p[3], p[0]), max(p[3], p[0])))
    
    if not graph[p[4]][p[5]]:
      cnt += 1
    checked.add((min(p[4], p[5]), max(p[4], p[5])))
    if not graph[p[5]][p[6]]:
      cnt += 1
    checked.add((min(p[5], p[6]), max(p[5], p[6])))
    if not graph[p[6]][p[7]]:
      cnt += 1
    checked.add((min(p[6], p[7]), max(p[6], p[7])))
    if not graph[p[7]][p[4]]:
      cnt += 1
    checked.add((min(p[7], p[4]), max(p[7], p[4])))
    
    for i in range(n):
      for j in range(i+1,n):
        if (i,j) in checked or (j,i) in checked:
          continue
        if graph[i][j]:
          cnt += 1

    ans = min(ans, cnt)
    
    cnt = 0
    checked = set()
    if not graph[p[0]][p[1]]:
      cnt += 1
    checked.add((min(p[0], p[1]), max(p[0], p[1])))
    if not graph[p[1]][p[2]]:
      cnt += 1
    checked.add((min(p[1], p[2]), max(p[1], p[2])))
    if not graph[p[2]][p[0]]:
      cnt += 1
    checked.add((min(p[2], p[0]), max(p[2], p[0])))
    
    if not graph[p[3]][p[4]]:
      cnt += 1
    checked.add((min(p[3], p[4]), max(p[3], p[4])))
    if not graph[p[4]][p[5]]:
      cnt += 1
    checked.add((min(p[4], p[5]), max(p[4], p[5])))
    if not graph[p[5]][p[6]]:
      cnt += 1
    checked.add((min(p[5], p[6]), max(p[5], p[6])))
    if not graph[p[6]][p[7]]:
      cnt += 1
    checked.add((min(p[6], p[7]), max(p[6], p[7])))
    if not graph[p[7]][p[3]]:
      cnt += 1
    checked.add((min(p[7], p[3]), max(p[7], p[3])))
    for i in range(n):
      for j in range(i+1,n):
        if (i,j) in checked or (j,i) in checked:
          continue
        if graph[i][j]:
          cnt += 1
    
    ans = min(ans, cnt)

print(ans)
