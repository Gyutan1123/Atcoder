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

w,h = MI()
n = II()
S = [LI() for _ in range(n)]
A = II()
a = LI()
a.insert(0,0)
a.append(w)
B = II()
b = LI()
b.insert(0,0)
b.append(h)

cnt = collections.defaultdict(int)
for i in range(n):
  p,q = S[i]
  cnt[(bisect.bisect_left(a,p), bisect.bisect_left(b,q))] += 1

m = float('inf')
M = 0
c = 0
for k in cnt.keys():
  m = min(m, cnt[k])
  M = max(M, cnt[k])
  c += 1

if c < (A+1)*(B+1):
  m = 0

print(m, M)