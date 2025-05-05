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
P = [LI() for _ in range(n)]
visited = [False] * (n+1)
ans = []
def dfs(v):
  for p in P[v-1][1:]:
    if not visited[p]:
      visited[p] = True
      dfs(p)
  ans.append(v)
  
dfs(1)
print(*ans[:-1])