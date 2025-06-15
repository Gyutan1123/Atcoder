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
AB = [LI() for _ in range(m)]
connect = [[] for _ in range(n)]
for a,b,w in AB:
  a -= 1
  b -= 1
  connect[a].append((b,w))
  
visited = [[False]*(1<<10) for _ in range(n)]

que = collections.deque()
que.append((0,0))

visited[0][0] = True
while que:
  now, state = que.popleft()
  
  for to, w in connect[now]:
    next_state = state^w
    if not visited[to][next_state]:
      visited[to][next_state] = True
      que.append((to, next_state))
    

ans = float('inf')
for state in range(1<<10):
  if visited[n-1][state]:
    ans = min(ans,state)

if ans == float('inf'):
  print(-1)
else:
  print(ans)