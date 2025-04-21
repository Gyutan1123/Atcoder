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
        if dist[i][k] != INF and dist[k][j] != INF:
          dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  return dist


n = II()
A = LI()
S = [list(SI()) for _ in range(n)]

graph = [[float('inf')]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if S[i][j] == 'Y':
      graph[i][j] = 10**15 - A[j]
      
ans = warshall_floyd(graph)
q = II()

for _ in range(q):
  u,v = MI()
  u -= 1
  v -= 1
  if ans[u][v] != float('inf'):
    l = 0
    r = n-1
    while r-l > 1:
      mid = (r+l)//2
      if mid*10**15 > ans[u][v]:
        r = mid
      else:
        l = mid
    
    e = r
    a = r*(10**15)-ans[u][v]
    a += A[u]
    print(e,a)
  else:
    print('Impossible')