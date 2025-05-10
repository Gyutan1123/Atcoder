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
info = [LI() for _ in range(m)]

connect = [[] for _ in range(n)]
for a,b,x,y in info:
  connect[a-1].append((b-1,x,y))
  connect[b-1].append((a-1,-x,-y))

p = [(-1,-1)]*n
p[0] = (0,0)
que = collections.deque()
que.append(0)
while que:
  now = que.popleft()
  for next,dx,dy in connect[now]:
    if p[next] == (-1,-1):
      p[next] = (p[now][0]+dx,p[now][1]+dy)
      que.append(next)

for i in range(n):
  if p[i] == (-1,-1):
    print('undecidable')
  else:
    print(p[i][0],p[i][1])