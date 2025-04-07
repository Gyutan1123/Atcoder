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
def warshall_floyd(graph):
  """
  ワーシャル・フロイド法で全点対間最短経路を計算する

  Args:
      graph: 隣接行列形式のグラフ (2次元リスト)
              graph[i][j] は頂点iからjへの辺のコスト。
              辺が存在しない場合は INF。

  Returns:
      全点対間最短経路の距離行列 (2次元リスト)
  """
  n = len(graph)
  dist = [row[:] for row in graph]  # graph のコピーを作成
  INF = float('inf')
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if graph[i][k] != INF and graph[k][j] != INF:
          dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  return dist

n = II()

J = [LI() for _ in range(n)]

g = [[0]*n for i in range(n)]

l = 0
r = 10**10

while r-l > 1:
  mid = (r+l)//2
  flag = False
  for i in range(n):
    que = collections.deque()
    que.append(i)
    visited = [False]*n
    visited[i] = True
    while que:
      now = que.popleft()
      for to in range(n):
        if visited[to] == False:
          x1,y1,p = J[now]
          x2,y2,_ = J[to]
          if p*mid >= abs(x1-x2)+abs(y1-y2):
            visited[to] = True
            que.append(to)

    if all(visited):
      flag = True
      break

  if flag:
    r = mid
  else:
    l = mid

print(r)