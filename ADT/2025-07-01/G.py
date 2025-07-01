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
S = [SI() for _ in range(h)]

nxt = {'s':'n','n':'u','u':'k','k':'e','e':'s'}

visited = [[False]*w for _ in range(h)]

if S[0][0] != 's':
  print('No')
  exit()
  
visited[0][0] = True
q = collections.deque([(0,0)])

while q:
  now = q.popleft()
  i,j = now
  
  if S[i][j] not in nxt:
    print('No')
    exit()
  
  nxt_char = nxt[S[i][j]]
  for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
    ni,nj = i+di,j+dj
    if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and S[ni][nj] == nxt_char:
      visited[ni][nj] = True
      q.append((ni,nj))
      
if visited[h-1][w-1]:
  print('Yes')
else:
  print('No')