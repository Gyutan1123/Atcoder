import sys
import collections, heapq, string, math, itertools, copy
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
A = LI()
B = LI()

dp = [[False]*2 for _ in range(n+1)]

dp[1][0] = True
dp[1][1] = True

for i in range(1,n):
  if abs(A[i]-A[i-1]) <= k:
    dp[i+1][0] = dp[i+1][0] | dp[i][0]
  if abs(A[i]-B[i-1]) <= k:
    dp[i+1][0] = dp[i+1][0] | dp[i][1]
    
  if abs(B[i]-A[i-1]) <= k:
    dp[i+1][1] = dp[i+1][1] | dp[i][0]
  if abs(B[i]-B[i-1]) <= k:
    dp[i+1][1] = dp[i+1][1] | dp[i][1]
    
if dp[n][0] or dp[n][1]:
  print('Yes')
else:
  print('No')