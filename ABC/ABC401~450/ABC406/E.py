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

t = II()
for _ in range(t):
  n,k = MI()
  N = format(n, '060b')

  dpCount = [[[0]*(k+1) for _ in range(2)] for _ in range(61)] 
  dpSum = [[[0]*(k+1) for _ in range(2)] for _ in range(61)]
 
  dpCount[0][0][0] = 1
  for i in range(60):
    bit = (n>>(59-i))&1
    for j in range(k+1):
      dpCount[i+1][1][j] += dpCount[i][1][j]
      dpCount[i+1][1][j] %= mod
      dpSum[i+1][1][j] += dpSum[i][1][j]*2
      dpSum[i+1][1][j] %= mod
      
      if j+1 <= k:
        dpCount[i+1][1][j+1] += dpCount[i][1][j]
        dpCount[i+1][1][j+1] %= mod 
        
        dpSum[i+1][1][j+1] += dpSum[i][1][j]*2 + dpCount[i][1][j]
        dpSum[i+1][1][j+1] %= mod
        
      if bit == 1:
        if j+1 <= k:
          dpCount[i+1][0][j+1] += dpCount[i][0][j]
          dpCount[i+1][0][j+1] %= mod
          dpSum[i+1][0][j+1] += dpSum[i][0][j]*2 + dpCount[i][0][j]
          dpSum[i+1][0][j+1] %= mod
        dpCount[i+1][1][j] += dpCount[i][0][j]
        dpCount[i+1][1][j] %= mod
        dpSum[i+1][1][j] += dpSum[i][0][j]*2
        dpSum[i+1][1][j] %= mod
      else:
        dpCount[i+1][0][j] += dpCount[i][0][j]
        dpCount[i+1][0][j] %= mod
        dpSum[i+1][0][j] += dpSum[i][0][j]*2
        dpSum[i+1][0][j] %= mod
    
  print((dpSum[i+1][0][k]+dpSum[i+1][1][k])%mod) 