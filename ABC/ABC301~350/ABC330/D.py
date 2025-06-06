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
P = [SI() for _ in range(n)]

counth = [0] * n
countw = [0] * n

for i in range(n):
  for j in range(n):
    if P[i][j] == "o":
      counth[i] += 1
      countw[j] += 1

ans = 0
for i in range(n):
  for j in range(n):
    if P[i][j] == "o":
      ans += (counth[i]-1)*(countw[j]-1)

print(ans)