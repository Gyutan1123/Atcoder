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

connect = [[] for _ in range(n)]
for _ in range(m):
  a,b = MI()
  connect[a-1].append(b-1)
  connect[b-1].append(a-1)
  
dist = [[-1]*(n) for _ in range(1<<n)]

que = collections.deque()
for i in range(n):
  que.append((i,1<<i))
  dist[1<<i][i] = 1

while que:
  now, bit = que.popleft()
  
  for to in connect[now]:
    next_bit = bit ^ (1 << to)
    if dist[next_bit][to] == -1:
      dist[next_bit][to] = dist[bit][now] + 1
      que.append((to, next_bit))
      
ans = 0
for i in range(1,1<<n):
  ans += min([dist[i][j] for j in range(n) if dist[i][j] != -1])
  
print(ans)