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


n = II()
A = LI()
B = LI()

AB = [(A[i],B[i]) for i in range(n)]
AB.sort(key=lambda x: (x[0], x[1]), reverse=True)

dp = [[0]*(5001) for _ in range(n+1)]

dp[n][0] = 1

for i in reversed(range(n)):
  b = AB[i][1]
  for j in range(5001):
    dp[i][j] += (dp[i+1][j] % mod)
    if j-b >= 0:
      dp[i][j] += (dp[i+1][j-b] % mod)
    dp[i][j] %= mod
  
  
ans = 0
for i in range(n):
  a,b = AB[i]
  if b > a:
    continue
  for j in range(a-b+1):
    ans += (dp[i+1][j] % mod)
    ans %= mod
  
print(ans)
