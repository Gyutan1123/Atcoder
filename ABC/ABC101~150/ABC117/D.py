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

n,k = MI()
kb = format(k, '060b')
A = LI()

dp = [[-float('inf')]*2 for _ in range(61)]
dp[0][0] = 0
for i in range(60):
  tmp1 = 0
  tmp0 = 0
  for a in A:
    tmp1 += (((a>>(59-i))&1)^1)<<(59-i)
    tmp0 += (((a>>(59-i))&1)^0)<<(59-i)
  
  if 1<<(59-i) > k:
    tmp1 = 0
      
  dp[i+1][1] = max(dp[i+1][1],max(tmp1,tmp0)+dp[i][1])
     
  if kb[i] == '1':
    dp[i+1][1] = max(dp[i+1][1], dp[i][0]+tmp0)
    dp[i+1][0] = dp[i][0]+tmp1
  else:
    dp[i+1][0] = dp[i][0]+tmp0

print(max(dp[60]))