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

n,m = MI()

dist = [[float('inf')]*(n+1) for _ in range(n+1)]
que = collections.deque()
que.append((1,1))
dist[1][1] = 0

s = dict()
for i in range(401):
  s[i**2] = i

while que:
  i,j = que.popleft()
  for toi in range(1,n+1):
    if not m-(i-toi)**2 in s:
      continue
    else:
      k = s[m-(i-toi)**2]
      if (1 <= j+k <= n 
          and dist[toi][j+k] > dist[i][j]+1):
        dist[toi][j+k] = dist[i][j]+1
        que.append((toi,j+k))
      
      if (1 <= j-k <= n 
          and dist[toi][j-k] > dist[i][j]+1):
        dist[toi][j-k] = dist[i][j]+1
        que.append((toi,j-k))

  
for i in range(1,n+1):
  for j in range(1,n+1):
    if dist[i][j] == float('inf'):
      dist[i][j] = -1
      
for d in dist[1:]:
  print(*d[1:])