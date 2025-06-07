import sys
import collections, heapq, string, math, itertools, copy, bisect, functools
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

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
x = LI()
connect = [[] for _ in range(n)]
for i in range(n-1):
  a,b,w = MI()
  connect[a-1].append((b-1,w))
  connect[b-1].append((a-1,w))

ans = 0
visited = [False]*n
def dfs(v):
  global ans
  if visited[v]:
    return 0
  visited[v] = True
  nowcnt = x[v]
  
  if len(connect[v]) == 1 and v != 0:
    return nowcnt
  else:
    for to,w in connect[v]:
      if not visited[to]:
        cnt = dfs(to)
        ans += abs(cnt)*w
        nowcnt += cnt
  
  return nowcnt

dfs(0)
print(ans)
