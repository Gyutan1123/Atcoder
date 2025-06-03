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

n = II()

visited = collections.defaultdict(bool)
visited[1] = True
visList = [1]
que = collections.deque([1])

connect = collections.defaultdict(list)
for i in range(n):
  a,b = MI()
  connect[a].append(b)
  connect[b].append(a)
  
while que:
  now = que.popleft()
  for to in connect[now]:
    if not visited[to]:
      visited[to] = True
      que.append(to)
      visList.append(to)
  
print(max(visList))
