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

n,k = MI()
A = LI()

B = [[] for _ in range(k)]

for i in range(n):
  B[i%k].append(A[i])

for b in B:
  b.sort(reverse=True)

As = []
for i in range(n):
  As.append(B[i%k][-1])
  B[i%k].pop()

if As == sorted(A):
  print('Yes')
else:
  print('No')