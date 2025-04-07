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

n,q = MI()
A = LI()
A.sort()

s = [0]
for i in range(n):
  s.append(s[-1]+A[i])

for _ in range(q):
  x = II()
  i = bisect.bisect_right(A,x)
  print(x*(2*i-n)+s[n]-2*s[i])