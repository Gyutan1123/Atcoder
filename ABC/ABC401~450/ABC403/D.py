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

n,d = MI()
A = LI()
if d == 0:
  print(n-len(set(A)))
  exit()
  
B = [[0]*((10**6 -x)// d + 10) for x in range(d)]


for a in A:
  y = a // d
  x = a % d
  B[x][y] += 1
  
ans = 0
for b in B:
  tmp = sum(b)
  l = len(b)
  dp = [[0]*2 for _ in range(l+1)]
  
  dp[0][0] = 0
  dp[0][1] = 0
  
  for i in range(l):
    dp[i+1][0] = max(dp[i+1][0], dp[i][1], dp[i][0])
    dp[i+1][1] = max(dp[i+1][1], dp[i][0]+b[i])
  
  ans += tmp-max(dp[l][0], dp[l][1])
  
print(ans)