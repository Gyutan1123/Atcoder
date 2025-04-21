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
m = II()
B = set(LI())
x = II()

dp = [False]*(x+1)

dp[0] = True

for i in range(x):
  if i in B or dp[i] == False:
    continue
  for a in A:
    if i+a <= x:
      dp[i+a] = True

print('Yes' if dp[x] else 'No')