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

n,q = MI()
x = LI()
connect = [[] for _ in range(n+1)]
for _ in range(n-1):
  a,b = MI()
  connect[a].append(b)
  connect[b].append(a)

I = [[] for _ in range(n+1)]
visited = [False]*(n+1)

def dfs(now):
  visited[now] = True
  heapq.heappush(I[now], x[now-1])
  for to in connect[now]:
    if visited[to] == False:
      dfs(to)
      for i in range(len(I[to])):
        heapq.heappush(I[now],I[to][i])
      
  while len(I[now]) > 20:
    heapq.heappop(I[now])
  I[now].sort()
  
dfs(1)

for _ in range(q):
  v,k = MI()
  print(I[v][-k])