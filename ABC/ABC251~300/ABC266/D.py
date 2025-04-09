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
mod = 10**9 + 7
########################################################

n = II()

A = [[0]*5 for _ in range(10**5+1)]

for _ in range(n):
  t,x,a = MI()
  A[t][x] = a


dp = [[0]*5 for _ in range(10**5+1)]

for i in range(10**5):
  for j in range(5):
    if j > i+1:
      continue
    dp[i+1][j] = A[i+1][j] + max(dp[i][max(0,j-1)],dp[i][j],dp[i][min(4,j+1)])
  
print(max(dp[10**5]))