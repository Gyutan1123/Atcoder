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

n = II()
cards = [LI() for _ in range(n)]

dp = [False]*(1<<n)

for i in reversed(range(1<<n)):
  select = []
  for j in range(n):
    if i & (1<<j) == 0:
      select.append(j)
  
  win = False
  for j,k in itertools.combinations(select, 2):
    if cards[j][0] == cards[k][0] or cards[j][1] == cards[k][1]:
      next_mask = i | (1<<j) | (1<<k)
      if not dp[next_mask]:
        win = True
        break
  dp[i] = win
  
print("Takahashi" if dp[0] else "Aoki")