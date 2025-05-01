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

n = II()
S = SI()

dp = [[0]*2 for _ in range(n+1)]

dp[n][0] = 0
dp[n][1] = 1

for i in reversed(range(n-1)):
  dp[i+1][0] = dp[i+2][1]
  if S[i+1] == '1':
    dp[i+1][1] = 1+dp[i+2][0]
  else:
    dp[i+1][1] = 1+dp[i+2][1]
  
ans = 0
for i in range(n):
  if S[i] == '1':
    ans += dp[i+1][1]
  else:
    ans += dp[i+1][0]

print(ans)