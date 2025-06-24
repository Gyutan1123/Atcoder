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
n,k = MI()
s = list(SI())

dp = [[0]*(1<<k) for _ in range(n+1)]

hatena = []
for i in range(k):
  if s[i] == '?':
    hatena.append(i)

bit = 0
for i in range(k):
  if s[i] == 'B':
    bit += (1<<i)
    
for mask in range(1<<len(hatena)):
  tmp = s[:k]
  addbit = 0
  for j in range(len(hatena)):
    if mask & (1<<j):
      tmp[hatena[j]] = 'B'
      addbit += (1<<hatena[j])
    else:
      tmp[hatena[j]] = 'A'
  if tmp != tmp[::-1]:
    dp[k][addbit+bit] += 1


for i in range(k, n):
  for j in range(1<<k):
    if dp[i][j] == 0:
      continue
    
    tmp = []
    for l in range(1,k):
      if j & (1<<l):
        tmp.append('B')
      else:
        tmp.append('A')
  
    if s[i] == '?':   
      tmp.append('A')
      if tmp != tmp[::-1]:
        dp[i+1][j>>1] += dp[i][j]%mod
      
      tmp[-1] = 'B'
      if tmp != tmp[::-1]:
        dp[i+1][(j>>1)+(1<<(k-1))] += dp[i][j]%mod
    
    elif s[i] == 'A':
      tmp.append('A')
      if tmp != tmp[::-1]:
        dp[i+1][j>>1] += dp[i][j]%mod
    else:
      tmp.append('B')
      if tmp != tmp[::-1]:
        dp[i+1][(j>>1)+(1<<(k-1))] += dp[i][j]%mod

ans = 0
for j in range(1<<k):
  ans += dp[n][j]
  ans %= mod
  
print(ans)
