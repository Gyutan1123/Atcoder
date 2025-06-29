class SegmentSieve:
  """
  区間[l,r)に含まれる整数を区間篩で素因数分解するクラス
  計算量はO((r-l)loglogr)
  
  factor(n) でnの素因数分解を返す
  unique=Trueを指定すると素因数のリスト
  with_exp=Trueを指定すると素因数とその指数のタプルのリストを返す
  """
  
  def __init__(self, l, r):
    self.l = l
    self.r = r
    
    self.sqrt_r = int(r**0.5)+1
    
    self.lpf = list(range(self.sqrt_r))
    self.mpf = [[] for _ in range(self.r-self.l)]
    self.aux = [1]*(self.r-self.l)
    
     
    self._build()
  
  def _build(self):
    for p in range(2, self.sqrt_r):
      if self.lpf[p] < p:
        continue
      
      self.lpf[p] = p
      
      for q in range(p*p, self.sqrt_r, p):
        if self.lpf[q] == q:
          self.lpf[q] = p
        
      start = self.l + (-self.l) % p
      
      for q in range(start, self.r, p):
        i = q - self.l
        r = q
        while r % p == 0:
          if self.aux[i]*self.aux[i] > self.r:
            break
          
          self.mpf[i].append(p)
          self.aux[i] *= p
          r //= p
          
  def factor(self, n, unique=False, with_exp=False):
    i = n - self.l
    ret = self.mpf[i].copy()
    
    m = n // self.aux[i]
    
    if m >= self.sqrt_r:
      ret.append(m)
    else:
      while m > 1:
        p = self.lpf[m]
        ret.append(p)
        m //= p
    
    if unique:
      ret = list(set(ret))
      return ret
    
    if with_exp:
      from collections import Counter
      ret = sorted(Counter(ret).items())
      return ret
    
    return ret
