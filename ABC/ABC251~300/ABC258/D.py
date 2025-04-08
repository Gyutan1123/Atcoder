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

n,x = MI()
ans = float('inf')

AB = [LI() for _ in range(n)]

S = [0]

for i in range(n):
  S.append(S[-1]+sum(AB[i]))


for i in range(n):
  now = i+1
  res = x-now

  tmp = S[i+1]
  if res >= 1:
    tmp += res*AB[i][1]

  ans = min(ans, tmp)

print(ans)
