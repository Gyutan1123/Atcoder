import sys
import collections, heapq, string, math, itertools, copy, bisect, functools
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

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
cards = [LI() for _ in range(n)]
dp = [[-1]*2 for _ in range(1<<n)]

def dfs(mask,turn):
  if dp[mask][turn] != -1:
    return dp[mask][turn]

  select = []
  for i in range(n):
    if mask & (1<<i) == 0:
      select.append(i)
  win = False
  for i,j in itertools.combinations(select, 2):
    if cards[i][0] == cards[j][0] or cards[i][1] == cards[j][1]:

      next_mask = mask | (1<<i) | (1<<j)
      
      nxt = dfs(next_mask, turn^1)
      if nxt == turn:
        win = True
        break
  dp[mask][turn] = turn if win else turn^1
  return dp[mask][turn]
  
dfs(0,0)
if dp[0][0] == 0:
  print("Takahashi")
else:
  print("Aoki")