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

s = SI()
t = SI()


dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
pre = [[(-1,-1)]*(len(t)+1) for _ in range(len(s)+1)]
for i in range(len(s)):
  for j in range(len(t)):
    if s[i] == t[j]:
      dp[i+1][j+1] = dp[i][j] + 1
      pre[i+1][j+1] = (i, j)
    else:
      dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
      if dp[i+1][j+1] == dp[i][j+1]:
        pre[i+1][j+1] = (i, j+1)
      else:
        pre[i+1][j+1] = (i+1, j)
        
ans = []
i, j = len(s), len(t)
while i > 0 and j > 0:
  if pre[i][j] == (i-1,j-1):
    ans.append(s[i-1])
    j -= 1
    i -= 1
  elif pre[i][j] == (i-1,j):
    i -= 1
  else:
    j -= 1

ans.reverse()
print(''.join(ans))
