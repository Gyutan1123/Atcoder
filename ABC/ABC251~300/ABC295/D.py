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

s = list(SI())
s = list(map(int,s))

R = [0]

d = collections.defaultdict(int)
d[0] += 1
for i in range(len(s)):
  R.append(R[-1]^(1<<s[i]))
  d[R[-1]] += 1

ans = 0
for r in range(1<<10):
  ans += d[r]*(d[r]-1)//2

print(ans)