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

B = [(-1)**i*A[i] for i in range(n)]

S = [0]
for b in B:
  S.append(S[-1]+b)

ans = 0
d = collections.Counter(S)
for k in d:
  ans += d[k]*(d[k]-1)//2

print(ans)  