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
c = LI()
now = n

k = n // min(c)
if k == 0:
  print(0)
  exit()

ans = []

for i in range(k):
  for j in reversed(range(9)):
    if now-c[j] >= 0 and (now-c[j])//min(c) >= k-i-1:
      ans.append(str(j+1))
      now -= c[j]
      break

print(''.join(ans))