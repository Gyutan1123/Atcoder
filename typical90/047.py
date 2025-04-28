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
MAX_LEN = 10**6+1
BASE_POW = [1]
for i in range(MAX_LEN):
  BASE_POW.append(CalcMod(Mul(BASE_POW[-1], BASE)))

class RollingHash:
  def __init__(self, s):
    self.s = s
    self.mod = MOD
    self.base = BASE
    self.base_pow = BASE_POW
    self.hash = [0]
    
    self.n = len(s)
    hash = 0
    for i in range(self.n):
      hash = CalcMod(Mul(hash, self.base)+(ord(self.s[i])-ord('a')+1))
      self.hash.append(hash)
  
  def get(self, l, r):
    """ s[l,r]のハッシュ値を返す．
    """
    POSITIVIZER = MOD * 4
    hash = CalcMod(self.hash[r]+POSITIVIZER-Mul(self.hash[l-1],self.base_pow[r-l+1]))
    return hash

  def prefix(self, r):
    return self.hash[r]

n = II()
S = SI()
T = SI()

SR = ['']*n
SG = ['']*n
SB = ['']*n

for i in range(n):
  s = S[i]
  if s == 'R':
    SR[i] = 'R'
    SG[i] = 'B'
    SB[i] = 'G'
  elif s == 'G':
    SR[i] = 'B'
    SG[i] = 'G'
    SB[i] = 'R'
  elif s == 'B':
    SR[i] = 'G'
    SG[i] = 'R'
    SB[i] = 'B'
  
SR = ''.join(SR)
SG = ''.join(SG)
SB = ''.join(SB)

RHSR = RollingHash(SR)
RHSG = RollingHash(SG)
RHSB = RollingHash(SB)
RHT = RollingHash(T)

ans = 0
for j in range(1,n+1):
  if RHT.get(j,n) == RHSR.get(1,n-j+1):
    ans += 1
  elif RHT.get(j,n) == RHSG.get(1,n-j+1):
    ans += 1
  elif RHT.get(j,n) == RHSB.get(1,n-j+1):
    ans += 1

for i in range(2,n+1):
  if RHT.get(1,n-i+1) == RHSR.get(i,n):
    ans += 1
  elif RHT.get(1,n-i+1) == RHSG.get(i,n):
    ans += 1
  elif RHT.get(1,n-i+1) == RHSB.get(i,n):
    ans += 1

print(ans)