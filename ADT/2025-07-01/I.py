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

MASK30 = (1<<30)-1
MASK31 = (1<<31)-1
MOD = (1<<61)-1
MASK61 = MOD

# a*b mod 2^61-1を返す関数(最後にModを取る)
def Mul(a,b):
  au = a >> 31
  ad = a & MASK31
  bu = b >> 31
  bd = b & MASK31
  mid = ad*bu + au*bd
  midu = mid >> 30
  midd = mid & MASK30
  return au*bu*2+midu+(midd<<31)+ad*bd

def CalcMod(x):
  xu = x >> 61
  xd = x & MASK61
  res = xu+xd
  if res >= MOD:
    res -= MOD
  return res

BASE = 100
MAX_LEN = 2*10**6+10
BASE_POW = [1]
for i in range(MAX_LEN):
  BASE_POW.append(CalcMod(Mul(BASE_POW[-1], BASE)))

class RollingHash:
  def __init__(self, s):
    self.s = s
    self.mod = MOD
    self.hash = [0]
    
    self.n = len(s)
    hash = 0
    for i in range(self.n):
      hash = CalcMod(Mul(hash, BASE)+(ord(self.s[i])-ord('a')+1))
      self.hash.append(hash)
  
  def get(self, l, r):
    """ s[l,r]のハッシュ値を返す．
    """
    POSITIVIZER = MOD * 4
    hash = CalcMod(self.hash[r]+POSITIVIZER-Mul(self.hash[l-1],BASE_POW[r-l+1]))
    return hash

  def prefix(self, r):
    return self.hash[r]
  

n = II()
T = SI()

rh1 = RollingHash(T)
rh2 = RollingHash(T[::-1])

if rh1.get(1,2*n) == rh2.get(1,2*n):
  print(T[:n][::-1])
  print(0)
  exit()

for i in range(1,n):
  hash1 = rh1.get(1,i)
  hash2 = rh2.get(n-i+1,n)
  
  hash3 = rh1.get(i+n+1,2*n)
  hash4 = rh2.get(n+1,2*n-i)
  
  if hash1 == hash2 and hash3 == hash4:
    ans = T[i:n+i]
    print(ans[::-1])
    print(i)
    exit()
  
  
print(-1)