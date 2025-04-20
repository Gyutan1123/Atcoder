class RollingHash:
  def __init__(self, s, mod=(1<<61)-1, base=100):
    self.s = s
    self.mod = mod
    self.base_pow = [1]
    self.hash = [0]
    
    self.n = len(s)
    for _ in range(self.n):
      self.base_pow.append((self.base_pow[-1]*base)%self.mod)
    
    hash = 0
    for i in range(self.n):
      hash *= base
      hash %= mod
      hash += (ord(self.s[i]) - ord('a') + 1)
      hash %= mod
      self.hash.append(hash)
  
  def get(self, l, r):
    """ s[l,r]のハッシュ値を返す．
    """
    return (self.hash[r]-self.hash[l-1]*self.base_pow[r-l+1])%self.mod