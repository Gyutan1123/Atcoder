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

class RollingHash:
  def __init__(self, s, mod=(1<<61)-1, base=100):
    self.s = s
    self.mod = mod
    self.base_pow = [1]
    self.hash = [0]
    
    n = len(s)
    for _ in range(n):
      self.base_pow.append((self.base_pow[-1]*base)%self.mod)
    
    hash = 0
    for i in range(n):
      hash *= base
      hash %= mod
      hash += (ord(self.s[i]) - ord('a') + 1)
      hash %= mod
      self.hash.append(hash)
  
  def get(self, l, r):
    """ s[l,r]のハッシュ値を返す．
    """
    return (self.hash[r]-self.hash[l-1]*self.base_pow[r-l+1])%self.mod
  
  

n,q = MI()
s = SI()

RH = RollingHash(s)

for _ in range(q):
  a,b,c,d = MI()
  if RH.get(a,b) == RH.get(c,d):
    print('Yes')
  else:
    print('No')
