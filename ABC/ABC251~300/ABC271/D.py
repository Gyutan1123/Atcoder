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

n,s = MI()

ans = [['']*(s+1) for _ in range(n+1)]

dp = [[False]*(s+1) for _ in range(n+1)]

dp[0][0] = True

ab = []

for i in range(n):
  a,b = MI()
  ab.append((a,b))
  for j in range(s+1):
    if j-a >= 0 and dp[i][j-a]:
      dp[i+1][j] =True
      ans[i+1][j] = 'H'
    
    if j-b >= 0 and dp[i][j-b]:
      dp[i+1][j] = True
      ans[i+1][j] = 'T'

if dp[n][s] == False:
  print('No')
else:
  print('Yes')
  now = s
  str = []
  for i in range(n):
    str.append(ans[n-i][now])
    if ans[n-i][now] == 'H':
      now -= ab[n-1-i][0]
    else:
      now -= ab[n-i-1][1]
  print(''.join(reversed(str)))