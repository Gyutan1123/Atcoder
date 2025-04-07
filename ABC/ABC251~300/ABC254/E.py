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
connect = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = MI()
  connect[a].append(b)
  connect[b].append(a)

q = II()
for _ in range(q):
  x,k = MI()
  que = collections.deque()
  que.append((x,0))
  ans = x
  visited = set()
  visited.add(x)
  while que:
    now,d = que.popleft()
    if d == k:
      continue
    else:
      for to in connect[now]:
        if not to in visited:
          visited.add(to)
          ans += to
          que.append((to,d+1))

  print(ans)