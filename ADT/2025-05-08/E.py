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

h,w,d = MI()

S = [list(SI()) for _ in range(h)]

que = []
m = [[-1]*w for _ in range(h)]
vis = [[False]*w for _ in range(h)]
for i in range(h):
  for j in range(w):
    if S[i][j] == 'H':
      m[i][j] = d
      que.append((-d,i,j))

while que:
  d,i,j = heapq.heappop(que)
  d = -d
  if vis[i][j]:
    continue
  vis[i][j] = True
  for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
    if 0 <= ni < h and 0 <= nj < w and S[ni][nj] == '.' and not vis[ni][nj]:
      if m[ni][nj] < d-1:
        m[ni][nj] = d-1
        heapq.heappush(que,(-d+1,ni,nj))
  
ans = 0
for i in range(h):
  for j in range(w):
    if vis[i][j]:
      ans += 1

print(ans)