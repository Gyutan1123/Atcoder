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

x,y,z = MI()
s = SI()

dp = [[float('inf')]*(2) for _ in range(len(s)+1)] 
dp[0][0] = 0
dp[0][1] = z

for i in range(len(s)):
  if s[i] == 'a':
    dp[i+1][0] = min(dp[i][0]+x, dp[i][1]+y+z)
    dp[i+1][1] = min(dp[i][0]+x+z, dp[i][1]+y)
  else:
    dp[i+1][0] = min(dp[i][0]+y, dp[i][1]+x+z)
    dp[i+1][1] = min(dp[i][0]+y+z, dp[i][1]+x)
        
print(min(dp[-1][0], dp[-1][1]))
