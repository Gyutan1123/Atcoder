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
  n,K = MI()
  
  dp1 = [[0]*2 for _ in range(61)]
  dp2 = [[0]*2 for _ in range(6)]
  
  dp1[0][1] = 1
  
  for i in range(59,-1,-1):
    nextdp1 = [[0]*2 for _ in range(61)]
    nextdp2 = [[0]*2 for _ in range(61)]
    
    w = (1<<i)%mod
    
    for j in range(59,-1,-1):
      for k in range(2):
        tmp1 = dp1[j][k]
        tmp2 = dp2[j][k]
        for l in range(2):
          if j+l > K:
            continue
          if k == 1 and l > (n>>i)&1:
            continue
          
          if k == 1 and l == (n>>i)&1:
            nextk = 1
          else:
            nextk = 0
            
          nextdp1[j+l][nextk] += tmp1
          nextdp1[j+l][nextk] %= mod
          
          add = (tmp2+tmp1*l*w)%mod
          nextdp2[j+l][nextk] += add
          nextdp2[j+l][nextk] %= mod
    dp1 = nextdp1
    dp2 = nextdp2
    
  print((dp2[K][0]+dp2[K][1])%mod)