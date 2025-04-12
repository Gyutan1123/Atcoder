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

n1 = II()
connect1 = [[] for _ in range(n1+1)]
for _ in range(n1-1):
  u,v = MI()
  connect1[u].append(v)
  connect1[v].append(u)

n2 = II()
connect2 = [[] for _ in range(n2+1)]
for _ in range(n2-1):
  u,v = MI()
  connect2[u].append(v)
  connect2[v].append(u)
  

que = collections.deque()

que.append(1)
dist = [0]*(n1+1)
visited = [False]*(n1+1)
visited[1] = True

while que:
  now = que.popleft()
  for to in connect1[now]:
    if visited[to] == False:
      que.append(to)
      visited[to] = True
      dist[to] = dist[now] + 1
      
# 直径の端点
u1 = dist.index(max(dist))
que.append(u1)
dist_from_u1 = [0]*(n1+1)
visited = [False]*(n1+1)
visited[u1] = True

while que:
  now = que.popleft()
  for to in connect1[now]:
    if visited[to] == False:
      que.append(to)
      visited[to] = True
      dist_from_u1[to] = dist_from_u1[now] + 1
     
# 直径のもう一方の端点
v1 = dist_from_u1.index(max(dist_from_u1)) 
que.append(v1)
dist_from_v1 = [0]*(n1+1)
visited = [False]*(n1+1)
visited[v1] = True

while que:
  now = que.popleft()
  for to in connect1[now]:
    if visited[to] == False:
      que.append(to)
      visited[to] = True
      dist_from_v1[to] = dist_from_v1[now] + 1
      
# 同じことを木2にもやる
que.append(1)

dist = [0]*(n2+1)
visited = [False]*(n2+1)
visited[1] = True

while que:
  now = que.popleft()
  for to in connect2[now]:
    if visited[to] == False:
      que.append(to)
      visited[to] = True
      dist[to] = dist[now] + 1
      
# 直径の端点
u2 = dist.index(max(dist))
que.append(u2)
dist_from_u2 = [0]*(n2+1)
visited = [False]*(n2+1)
visited[u2] = True

while que:
  now = que.popleft()
  for to in connect2[now]:
    if visited[to] == False:
      que.append(to)
      visited[to] = True
      dist_from_u2[to] = dist_from_u2[now] + 1
     
# 直径のもう一方の端点
v2 = dist_from_u2.index(max(dist_from_u2)) 
que.append(v2)
dist_from_v2 = [0]*(n2+1)
visited = [False]*(n2+1)
visited[v2] = True

while que:
  now = que.popleft()
  for to in connect2[now]:
    if visited[to] == False:
      que.append(to)
      visited[to] = True
      dist_from_v2[to] = dist_from_v2[now] + 1
      
def op(a,b):
  return (a+b)
def e():
  return 0     


D = [0]*(n2+1)
for i in range(1,n2+1):
  D[i] = max(dist_from_u2[i],dist_from_v2[i])
  
D.sort()

segtree = SegTree(op,e,n2+1,D)

R1 = max(dist_from_u1)
R2 = max(dist_from_u2)

R = max(R1,R2)

ans = 0
for i in range(1,n1+1):
  l = 0
  r = n2+1
  while r-l > 1:
    mid = (r+l)//2
    if 1+max(dist_from_u1[i],dist_from_v1[i])+D[mid] < R:
      l = mid
    else:
      r = mid
    
  ans += (n2-r+1)*(max(dist_from_u1[i],dist_from_v1[i])+1)+segtree.prod(r,n2+1)
  ans += (r-1)*R
  
print(ans)