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
visited = [False]*(n+1) 

def dfs(v, visited):
  visited[v] = True
  connect = LI()

  for to in connect[1:]:
    if not visited[to]:
      print(to, flush=True)
      if to == n:
        ok = SI()
        exit()
      dfs(to, visited)
      print(v, flush=True)
      connect = LI()
dfs(1, visited)