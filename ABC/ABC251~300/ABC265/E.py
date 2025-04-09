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
mod = 998244353
########################################################

n,m = MI()
a,b,c,d,e,f = MI()


dp = [[0]*((n+1)*(n+1)) for _ in range(n+1)]

D = set()
for _ in range(m):
  x,y = MI()
  D.add((x,y))
  
dp[0][0]= 1
for i in range(n):
  for j in range(i+1):
    for k in range(i-j+1):
      l = i-j-k
      x = j*a+k*c+l*e
      y = j*b+k*d+l*f
      if (x+a, y+b) not in D:
        dp[i+1][(j+1)*(n+1)+k] += dp[i][j*(n+1)+k]%mod
        
      if (x+c, y+d) not in D:
        dp[i+1][j*(n+1)+k+1] += dp[i][j*(n+1)+k]%mod
        
      if (x+e, y+f) not in D:
        dp[i+1][j*(n+1)+k] += dp[i][j*(n+1)+k]%mod
        
ans = 0
for j in range(n+1):
  for k in range(n+1):
    ans += dp[n][j*(n+1)+k]%mod

print(ans%mod)