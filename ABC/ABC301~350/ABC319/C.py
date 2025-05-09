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

ans = 0

C = [LI() for _ in range(3)]

for p in itertools.permutations(range(9)):
  vis = [0]*9
  for i in range(3):
    for j in range(3):
      vis[p[i*3+j]] = i*3+j
  
  flag = True
  for i in range(3):
    a,b,c = C[i]
    if a != b and a != c and b != c:
      continue
    if a == b:
      if vis[i*3+2] > vis[i*3+0] and vis[i*3+2] > vis[i*3+1]:
        flag = False
        break
    if a == c:
      if vis[i*3+1] > vis[i*3+0] and vis[i*3+1] > vis[i*3+2]:
        flag = False
        break
    if b == c:
      if vis[i*3+0] > vis[i*3+1] and vis[i*3+0] > vis[i*3+2]:
        flag = False
        break
    
  for j in range(3):
    a,b,c = C[0][j], C[1][j], C[2][j]
    if a != b and a != c and b != c:
      continue
    if a == b:
      if vis[2*3+j] > vis[0*3+j] and vis[2*3+j] > vis[1*3+j]:
        flag = False
        break
    if a == c:
      if vis[1*3+j] > vis[0*3+j] and vis[1*3+j] > vis[2*3+j]:
        flag = False
        break
    if b == c:
      if vis[0*3+j] > vis[1*3+j] and vis[0*3+j] > vis[2*3+j]:
        flag = False
        
  
  a,b,c = C[0][0], C[1][1], C[2][2]
  if a == b:
    if vis[2*3+2] > vis[0*3+0] and vis[2*3+2] > vis[1*3+1]:
      flag = False
  if a == c:
    if vis[1*3+1] > vis[0*3+0] and vis[1*3+1] > vis[2*3+2]:
      flag = False
  if b == c:
    if vis[0*3+0] > vis[1*3+1] and vis[0*3+0] > vis[2*3+2]:
      flag = False
  
  a,b,c = C[0][2], C[1][1], C[2][0]
  if a == b:
    if vis[2*3+0] > vis[0*3+2] and vis[2*3+0] > vis[1*3+1]:
      flag = False
  if a == c:
    if vis[1*3+1] > vis[0*3+2] and vis[1*3+1] > vis[2*3+0]:
      flag = False
  if b == c:
    if vis[0*3+2] > vis[1*3+1] and vis[0*3+2] > vis[2*3+0]:
      flag = False
  
  if flag:
    ans += 1

print(ans/(362880))