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

def MatMul(a,b,mod=None):
  I, J, K = len(a), len(b[0]), len(b)
  c = [[0]*J for _ in range(I)]
  for i in range(I):
    for j in range(J):
      for k in range(K):
        if mod:
          c[i][j] = (c[i][j]+a[i][k]*b[k][j])%mod
        else:
          c[i][j] += a[i][k]*b[k][j]
  
  return c

def MatPow(x,n,mod=None):
  y = [[0]*len(x) for _ in range(len(x))]
  for i in range(len(x)):
    y[i][i] = 1
  while n > 0:
    if n & 1:
      y = MatMul(x,y,mod)
    x = MatMul(x,x,mod)
    n >>= 1
  return y

n = SI()
l = len(n)
n = int(n)

A = [[pow(10,l,mod),1],[0,1]]

print((n*sum(MatPow(A,n-1,mod)[0]))%mod)