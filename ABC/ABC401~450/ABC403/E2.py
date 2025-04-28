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
MAX_LEN = 5*10**5+1
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
  
q = II()
ans = 0

# 各hash値に対応する文字列をprefixとして持つような，Yに含まれる文字列の個数
d = collections.defaultdict(int)

# 各yに対するクエリ番号を保持
Y = collections.defaultdict(set)

# 各yに対するクエリ番号をキーとして，各prefixのhashをリストで保持
S = [[] for _ in range(q)]
X = set()
rh_cache = dict()
for i in range(q):
  t,s = sys.stdin.readline().split()
  t = int(t)
  
  if t == 1:
    if s in rh_cache:
      rh = rh_cache[s]
    else:
      rh = RollingHash(s)
      rh_cache[s] = rh
    pref = rh.hash
    X.add(pref[len(s)])
    if d[pref[len(s)]] > 0:

      # Xをprefixとして持つ文字列の分だけ引く
      ans -= d[pref[len(s)]]

      # Xをprefixとして持つYそれぞれについて削除を行う
      for j in list(Y[pref[len(s)]]):
        # jはクエリ番号
        for p in S[j]:
          # 各prefixに対して削除
          d[p] -= 1
          Y[p].discard(j)
        S[j] = []

        
  if t == 2:
    if s in rh_cache:
      rh = rh_cache[s]
    else:
      rh = RollingHash(s)
      rh_cache[s] = rh

    flag = True
    pref = rh.hash
    P = []
    for j in range(1,len(s)+1):
      P.append(pref[j])
      if pref[j] in X:
        flag = False
        break
    if flag:
      ans += 1
      for p in P:
        d[p] += 1
        Y[p].add(i)
      S[i] = P.copy()
      

  print(ans)