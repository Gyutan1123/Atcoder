import sys
import collections

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
mod = 998244353
########################################################

class SegmentSieve:
  """
  区間[l,r)に含まれる整数を区間篩で素因数分解するクラス
  計算量はO((r-l)loglogr)
  
  factor(n) でnの素因数分解を返す
  unique=Trueを指定すると素因数のリスト
  with_exp=Trueを指定すると素因数とその指数のタプルのリストを返す
  """
  __slots__ = ("l","r","sqrt_r","lpf","rem","factors")
  def __init__(self, l, r):
    self.l = l
    self.r = r
    
    self.sqrt_r = int(r**0.5)+1
    
    self.lpf = list(range(self.sqrt_r))
    
    self.rem = list(range(self.l, self.r))
    self.factors = [[] for _ in range(self.r-self.l)]
     
    self._build()
  
  def _calculate_lpf(self):
    for p in range(2, self.sqrt_r):
      if self.lpf[p] < p:
        continue
      for q in range(p*p, self.sqrt_r, p):
        if self.lpf[q] == q:
          self.lpf[q] = p
        
  def _build(self):
    self._calculate_lpf()
    
    for p in range(2, self.sqrt_r):
      if self.lpf[p] < p:
        continue
      
      start = self.l + (-self.l) % p
      for q in range(start, self.r, p):
        i = q - self.l
        while self.rem[i] % p == 0:
          self.factors[i].append(p)
          self.rem[i] //= p
    
    
  def factor(self, n, unique=False, with_exp=False):    
    i = n - self.l
    ret = self.factors[i].copy()
    
    if self.rem[i] > 1:
      ret.append(self.rem[i])
    
    if unique:
      return list(set(ret))
    
    if with_exp:
      if not ret:
        return []
      
      import collections
      return list(collections.Counter(ret).items())

    return ret
    
n,k = MI()



segmentsieve1 = SegmentSieve(1,k+1)
segmentsieve2 = SegmentSieve(n-k+1,n+1)

d = collections.defaultdict(int)
  
for i in range(n-k+1,n+1):
  for p in segmentsieve2.factor(i):
    d[p] += 1
    
for i in range(1,k+1):
  for p in segmentsieve1.factor(i):
    d[p] -= 1

ans = 1
for p in d:
  if d[p] > 0:
    ans *= (d[p]+1)%mod
    ans %= mod
  
print(ans)
