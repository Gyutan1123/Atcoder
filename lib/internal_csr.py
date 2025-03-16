def csr(n, E):
  """ CSR形式に変換
  https://qiita.com/AkariLuminous/items/31faea745b5dd4fb9edc

  Args:
      n : 頂点数
      E : E[i] = [辺iの始点、辺iの終点] (0-indexed)
  """
  start = [0] * (n+1)
  elist = [0] * len(E)
  # start[i+1] = 頂点 i を始点とする辺の数
  for e0, e1 in E:
    start[e0 + 1] += 1
  # 累積和
  for i in range(1, n+1):
    start[i] += start[i-1]
  # 挿入位置を表すポインタ
  counter = start[:]
  for e0, e1 in E:
    elist[counter[e0]] = e1
    counter[e0] += 1 # ポインタをインクリメント
  return start, elist