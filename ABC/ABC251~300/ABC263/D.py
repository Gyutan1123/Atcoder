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

class SegTree:
  def __init__(self, op, e, n, v=None):
    """
    Args:
        op : 演算
        e : 単位元
        n : 対象の列の要素数
        v : 対象の列. Defaults to None.
    """
    self._n = n
    self._op = op
    self._e = e
    self._log = (n-1).bit_length() # 2^(_log) >= n となる最小の整数
    self._size = 1 << self._log
    self._d = [self._e()] * (2 * self._size)
    if v is not None:
      # 葉に対象の列を格納
      for i in range(self._n):
        self._d[self._size + i] = v[i]
      for i in range(self._size - 1, 0, -1):
        self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])
            
  def set(self, p, x):
    """ 更新クエリ

    Args:
        p : a_p を 
        x : xに更新
    """
    # 葉に移動
    p += self._size
    
    self._d[p] = x
    # 関連する場所を更新
    while p:
      self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
      p >>= 1
      
  def prod(self, l, r):
    """ 取得クエリ

    Args:
        l, r : 区間[l, r)
    Return:
        区間[l, r)の総積
    """
    # 左の結果、右の結果
    sml, smr = self._e(), self._e()
    
    l += self._size
    r += self._size
    
    # 未計算の区間がなくなるまで
    while l < r:
      # 自身が右子ノードなら使用
      if l & 1:
        sml = self._op(sml, self._d[l])
        l += 1
      if r & 1:
        r -= 1
        smr = self._op(self._d[r], smr)
        
      # 親に移動
      l >>= 1
      r >>= 1
    return self._op(sml, smr)
  
  def all_prod(self):
    """ 全要素の総積を取得
    """
    return self._d[1]
  
  def get(self, p):
    """ a_pを取得するメソッド
    """
    return self._d[p + self._size]
  

n,l,r = MI()
a = LI()

s = [0]
for i in range(n):
  s.append(s[-1]+a[i])
  
def op(a,b):
  return min(a,b)
def e():
  return float('inf')
f = SegTree(op,e,n+1)
for y in range(n+1):
  f.set(y,r*y + s[n-y]) 
  
ans = float('inf')
for x in range(n+1):
  ans = min(ans, l*x-s[x]+f.prod(0,n-x+1))
  
print(ans)