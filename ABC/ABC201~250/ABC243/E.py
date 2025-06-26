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

def WarshallFloyd(graph):
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
        if dist[i][k] != INF and dist[k][j] != INF:
          dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  return dist

n,m = MI()

graph = [[float('inf')]*n for _ in range(n)]
for _ in range(m):
  a,b,c = MI()
  graph[a-1][b-1] = c
  graph[b-1][a-1] = c

dist = WarshallFloyd(graph)

ans = 0

for i in range(n):
  for j in range(i+1,n):
    if graph[i][j] == float('inf'):
      continue
    flag = True
    for k in range(n):
      if k != i and k != j:
        if dist[i][k]+dist[k][j] <= graph[i][j]:
          flag = False
          break
    if not flag:
      ans += 1

print(ans)
