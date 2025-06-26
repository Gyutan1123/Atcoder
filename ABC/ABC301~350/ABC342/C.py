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
s = SI()
q = II()

D = collections.defaultdict(str)
for a in string.ascii_lowercase:
  D[a] = a

for _ in range(q):
  c,d = MS()
  for a in string.ascii_lowercase:
    if D[a] == c:
      D[a] = d
  
ans = ''
for a in s:
  ans += D[a]
print(ans)