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
mod = 998244353
########################################################

# Combination
# 組み合わせ
# nCr
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = mod
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)
    

n,k = MI()

A = LI()
S = [0]
for i in range(n):
  S.append(S[-1]+A[i])

Sk = [[] for _ in range(k+1)]
Sk[0] = [1]*(n+1)
for i in range(1,k+1):
  for j in range(n+1):
    Sk[i].append(pow(S[j],i,mod))
  
SkS = [[0] for _ in range(k+1)]
for i in range(k+1):
  for j in range(n+1):
    SkS[i].append((SkS[i][-1]+Sk[i][j])%mod)
    
ans = 0

for i in range(k+1):
  tmp = pow(-1,k-i)*cmb(k,i,mod)
  tmp2 = 0
  for l in range(n):
    tmp2 += Sk[k-i][l]*(SkS[i][n+1]-SkS[i][l+1])
  tmp *= tmp2
  ans += tmp%mod
  
print(ans%mod)