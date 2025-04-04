import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

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

tutu = []
d = collections.defaultdict(list)
tmp = (0,-1)
top = -1
for i in range(n):
  a = A[i]
  tutu.append(a)
  if top == a:
    d[a][-1] += 1
    if d[a][-1] == a:
      d[a].pop()
      for _ in range(a):
        tutu.pop()
      if len(tutu) > 0:
        top = tutu[-1]
      else:
        top = -1
  else:
    top = a
    d[a].append(1)
  
  print(len(tutu))