import sys
import collections, heapq, string, math, itertools, copy

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

n,p,k = MI()

l = 0
r = 2000000001

A = [LI() for _ in range(n)]

while r-l > 1:
  x = (r+l)//2
  cost = copy.deepcopy(A)
  for i in range(n):
    for j in range(n):
      if cost[i][j] == -1:
        cost[i][j] = x
  dist = warshall_floyd(cost)

  tmp = 0
  for i in range(n):
    for j in range(i+1,n):
      if dist[i][j] <= p:
        tmp += 1

  if tmp <= k:
    r = x
  else:
    l = x
    
# x >= x1 なら距離P以下の街の組が k組以下
x1 = r

l = 0
r = 2000000001


while r-l > 1:
  x = (r+l)//2
  cost = copy.deepcopy(A)
  for i in range(n):
    for j in range(n):
      if cost[i][j] == -1:
        cost[i][j] = x
  dist = warshall_floyd(cost)

  tmp = 0
  for i in range(n):
    for j in range(i+1,n):
      if dist[i][j] <= p:
        tmp += 1
  
  if tmp <= k-1:
    r = x
  else:
    l = x
    
# x <= x2 なら距離P以下の街の組が k組以上
x2 = l


if x2 >= x1:
  if x2 == 2000000000:
    print('Infinity')
  else:
    print(x2-x1+1)
else:
  print(0)