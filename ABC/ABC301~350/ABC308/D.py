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

S = [SI() for _ in range(h)]

n = collections.defaultdict(lambda:'?')
n['s'] = 'n'
n['n'] = 'u'
n['u'] = 'k'
n['k'] = 'e'
n['e'] = 's'

visited = [[False]*w for _ in range(h)]
que = collections.deque()
que.append((0,0,S[0][0]))
visited[0][0] = True
D = [(-1,0), (0,1), (1,0), (0,-1)]
while que:
  i,j,s = que.popleft()
  for d in D:
    ni = i + d[0]
    nj = j + d[1]
    if ni < 0 or ni >= h or nj < 0 or nj >= w:
      continue
    if visited[ni][nj]:
      continue
    if S[ni][nj] == n[s]:
      visited[ni][nj] = True
      que.append((ni,nj,S[ni][nj]))
      
if visited[h-1][w-1]:
  print('Yes')
else:
  print('No')