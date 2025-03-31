import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

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
que = collections.deque()
visited = [[False]*w for _ in range(h)]
C = [list(SI()) for _ in range(h)]

que.append((0,0))
visited[0][0] = True

D = [(1,0),(0,1)]

while que:
  now = que.popleft()
  for d in D:
    toc = now[0]+d[0]
    tor = now[1]+d[1]
    if (0 <= toc < h 
        and 0 <= tor < w 
        and C[toc][tor] == '.'
        and visited[toc][tor] == False):
      visited[toc][tor] = True
      que.append((toc,tor))

ans = 0
for i in range(h):
  for j in range(w):
    if visited[i][j]:
      ans = max(ans,i+j+1)

print(ans)