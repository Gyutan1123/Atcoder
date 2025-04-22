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

n,a,x,y = MI()

# 残りn円の時からの期待値
dp = dict()
dp[0] = 0
def dfs(n):
  if n in dp:
    return dp[n]
  
  dp[n] = min(x+dfs(n//a), 
              1.2*y+0.2*(dfs(n//2)+dfs(n//3)+dfs(n//4)+dfs(n//5)+dfs(n//6)))
  return dp[n]

dfs(n)

print(dp[n])
