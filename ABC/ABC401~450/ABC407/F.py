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


n = II()
A = LI()
B = [-A[i] for i in range(n)]
ans = [0]*(n+2)

CT = CartesianTree(B)

def dfs(CT, i):
  if i == -1:
    return 0
  l = dfs(CT, CT.left[i])+1
  r = dfs(CT, CT.right[i])+1
  
  ans[0] += A[i]
  ans[l] -= A[i]
  ans[r] -= A[i]
  ans[l+r] += A[i]
  return l+r-1
  
dfs(CT, CT.root)
for i in range(n+1):
  ans[i+1] += ans[i]
for i in range(n+1):
  ans[i+1] += ans[i]

for i in range(n):
  print(ans[i])