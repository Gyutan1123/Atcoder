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

n,m = MI()
C = LI()
A = [LI() for _ in range(m)]

d = collections.defaultdict(list)
for i in range(m):
  k = A[i][0]
  for j in range(k):
    d[A[i][j+1]].append(i)

ans = float('inf')
for i in range(3**n):
  tmp = 0
  animal = [0]*m
  for j in range(n):
    if (i//(3**j))%3 == 1:
      tmp += C[j]
      for a in d[j+1]:
        animal[a] += 1
    elif (i//(3**j))%3 == 2:
      tmp += C[j]*2
      for a in d[j+1]:
        animal[a] += 2
  
  if all(x >= 2 for x in animal):
    ans = min(ans, tmp)

print(ans)
