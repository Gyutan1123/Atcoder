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