import sys
import collections, heapq, string, math, itertools, copy
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


l = [0]*(10**6+1)

for i in range(2,10**6+1):
  if l[i] == 0:
    j = i
    while j <= 10**6:
      l[j] += 1
      j += i
  
A = SortedSet()

for i in range(2,10**6+1):
  if l[i] == 2:
    A.add(i**2)
  
q = II()
for _ in range(q):
  a = II()
  print(A[A.bisect_right(a)-1])