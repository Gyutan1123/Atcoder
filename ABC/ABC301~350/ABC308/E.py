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
A = LI()

S = SI()

dp = [[0]*40 for _ in range(n+1)]

dp[0][0] = 1

for i in range(n):
  for j in range(40):
    dp[i+1][j] += dp[i][j]
  
  s = S[i]
  a = A[i]
  if s == 'M':
    dp[i+1][a+1] += 1
  
  if s == 'E':
    for j in range(3):
      dp[i+1][j+3*a+4] += dp[i][j+1]
  
  if s == 'X':
    for j in range(9):
      dp[i+1][j+9*a+13] += dp[i][j+4]
       
ans = 0

for j in range(13,40):
  if dp[n][j] == 0:
    continue
  s = SortedSet([0,1,2,3])
  tmp = j-13
 
  a1 = tmp%3
  tmp //= 3
  a2 = tmp%3
  tmp //= 3
  a3 = tmp%3

  s.discard(a1)
  s.discard(a2)
  s.discard(a3)
  mex = s[0]
  ans += dp[n][j] * mex
  
print(ans)