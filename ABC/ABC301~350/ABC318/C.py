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

n,d,p = MI()
f = LI()

f.sort()
S = [0]
for i in range(n):
  S.append(S[-1]+f[i])

ans = float('inf')
for i in range(n+1):
  ans = min(ans, S[max(0, n-d*i)]+p*i)
print(ans)