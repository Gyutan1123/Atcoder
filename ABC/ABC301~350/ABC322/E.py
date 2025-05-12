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

n,k,p = MI()

dp = [[float('inf')]*(6**5) for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
  A = LI()
  C = A[0]
  A = A[1:]
  for j in range(6**5):
    flag = True
    tmp = 0
    offset = 0
    for l in range(k):
      offset += (min(5,(j//(6**l)%6+A[l]))-j//(6**l)%6)*(6**l)
    dp[i+1][j+offset] = min(dp[i+1][j+offset], dp[i][j] + C)
    dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    

ans = float('inf')
for j in range(6**5):
  flag = True
  for l in range(k):
    if j//(6**l)%6 < p:
      flag = False
      break
  if flag:
    ans = min(ans, dp[n][j])

if ans == float('inf'):
  print(-1)
else:
  print(ans)