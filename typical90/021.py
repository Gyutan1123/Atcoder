import sys
import collections, heapq, string
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

mod = 10**9 + 7
########################################################

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

class _SCC_graph:
  def __init__(self, n):
    self._n = n
    self.edges = []
    sys.setrecursionlimit(max(2*n, sys.getrecursionlimit()))
    
  def num_vertices(self):
    return self._n
      
  def add_edge(self, frm, to):
    """
        from -> to の辺を追加

        Args:
            frm (int): 追加する辺の始点
            to  (int): 追加する辺の終点
    """
    
    self.edges.append([frm, to])
    
  def scc_ids(self):
    """
    Tarjan のアルゴリズムでグラフの強連結成分分解を行う

    Returns:
        group_num (int): グラフの強連結成分数
        ids (List[int]): 各頂点が属する強連結成分のid
    """
    
    # 辺をcsr形式に変換
    start, elist = csr(self._n, self.edges)

    # 探索した頂点数, 見つかったSCCの数
    now_ord, group_num = 0, 0
    
    # 探索済みかつidが未確定の頂点を管理するstack
    visited = []
    
    low = [0] * self._n # lowlink
    ord_ = [-1] * self._n # order (-1は未探索を表す)
    ids = [0] * self._n # SCC id
    
    def dfs(v):
      nonlocal now_ord, group_num, visited, low, ord_, ids
      
      # 行きがけ:
      #    * orderを付与
      #    * lowlinkをorderで初期化
      #    * stackに追加
      low[v] = ord_[v] = now_ord
      now_ord += 1
      visited.append(v)
      
      for i in range(start[v], start[v+1]):
        to = elist[i]
      
        # 行き先が未探索の場合(この辺はtree edge)
        if ord_[to] == -1:
          dfs(to)
          
          # tree edgeは何回でも使えるので
          # vのlowlink<=toのlowlink
          low[v] = min(low[v], low[to])
          
        # 探索済みの場合 (この辺はtree edgeでない)
        else:
          # tree edgeでない辺は1回しか使えないので
          # 行き先のorderでlowlinkを更新
          low[v] = min(low[v], ord_[to])
          
      # 帰りがけ:
      #    * vがscc_rootのときstackのv以降にSCC idを付与
      #    * orderをn(無限大と同等)に変更しこれ以降
      #      lowlinkの計算に使われないようにする
      if low[v] == ord_[v]:
        while True:
          u = visited.pop()
          ord_[u] = self._n
          ids[u] = group_num
          if u == v:
            break
        group_num += 1
    
    
    for i in range(self._n):
      # 未探索の頂点からDFSを行う
      if ord_[i] == -1:
        dfs(i)
        
    # SCC id はトポロジカル順序の逆順に付与されているので反転する
    for i in range(self._n):
      ids[i] = group_num - 1 - ids[i]
      
      
    return group_num, ids
  
  def scc(self):
    """
    強連結成分分解の結果を整形して返す
    
    Returns:
        groups (List[List[int]]): 各リストがそれぞれSCCに対応。
                                  縮約されたグラフでのトポロジカルソートがされている
    """
    group_num, ids = self.scc_ids()
    groups = [[] for _ in range(group_num)]
    for i in range(self._n):
      groups[ids[i]].append(i)
    return groups
  
class SCC_graph:
    def __init__(self, n):
        self._n = n
        self._scc_graph = _SCC_graph(n)
    
    def add_edge(self, frm, to):
        assert 0 <= frm < self._n
        assert 0 <= to < self._n
        self._scc_graph.add_edge(frm, to)
    
    def scc(self):
        return self._scc_graph.scc()

n,m = MI()
scc_graph = SCC_graph(n+1)
for i in range(m):
  a,b = MI()
  scc_graph.add_edge(a,b)
  
groups = scc_graph.scc()

ans = 0
for group in groups:
  num = len(group)
  ans +=  num*(num-1) // 2
  
print(ans)