import sys
import collections, heapq, string, math, itertools, copy

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
tube = [[] for _ in range(m)]
d = [[-1]*2 for _ in range(n+1)]
trash = [0]*m

for i in range(m):
  k = II()
  A = LI()
  for j in range(k):
    a = A[-j-1]
    tube[i].append(a)
    if d[a][0] == -1:
      d[a][0] = (i,k-1-j)
    else:
      d[a][1] = (i,k-1-j)
      
available = set()
for i in range(1,n+1):
  if d[i][0][1] == 0 and d[i][1][1] == 0:
    available.add((d[i][0][0],d[i][1][0]))

cnt = 0

while True:
  if len(available) == 0:
    if cnt == n:
      print('Yes')
    else:
      print('No')
    break
  
  i,j = available.pop()
  trash[i] += 1
  trash[j] += 1
  
  tube[i].pop()
  tube[j].pop()
  
  cnt += 1
  
  if (len(tube[i]) > 0 
      and d[tube[i][-1]][0][1]-trash[d[tube[i][-1]][0][0]] == 0 
      and d[tube[i][-1]][1][1]-trash[d[tube[i][-1]][1][0]] == 0):
    available.add((d[tube[i][-1]][0][0], d[tube[i][-1]][1][0]))
    
  if (len(tube[j]) > 0 
      and not (len(tube[i]) > 0 and tube[j][-1] == tube[i][-1])
      and d[tube[j][-1]][0][1]-trash[d[tube[j][-1]][0][0]] == 0 
      and d[tube[j][-1]][1][1]-trash[d[tube[j][-1]][1][0]] == 0):
    available.add((d[tube[j][-1]][0][0], d[tube[j][-1]][1][0]))