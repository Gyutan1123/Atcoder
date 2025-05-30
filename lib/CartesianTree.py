class CartesianTree:
  def __init__(self, A):
    self.A = A
    self.n = len(A)
    self.parent = [-1]*self.n
    self.left = [-1]*self.n
    self.right = [-1]*self.n
    self.root = 0
    
    self.build()
    
  # Cartesian Treeの構築
  def build(self):
    # 添え字を格納するスタック
    stack = []
    for i, val in enumerate(self.A):
      last = -1
      # 新しく入ってくる要素がスタックの一番上の要素より小さい場合
      # 単調増加になるまでスタックの要素をpopしていく
      while stack and self.A[stack[-1]] > val:
        last = stack.pop()
      
      if last != -1:
        self.left[i] = last
        self.parent[last] = i
    
      # スタックが空の場合は、iが新しい根になる
      if len(stack) == 0:
        self.root = i
      # それ以外の場合，2番目の要素が親
      else:
        self.parent[i] = stack[-1]
        self.right[stack[-1]] = i
      stack.append(i)
