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

K = II()

num = [[[] for _ in range(11)] for _ in range(11)]

for i in range(10):
  num[1][i].append(i)

# i+1桁 最上位j
for i in range(2,11):
  for j in range(1,10):
    for k in range(j):
      for l in num[i-1][k]:
        num[i][j].append(l + j*10**(i-1))

s = SortedSet()

for i in range(1,11):
  for j in range(10):
    for k in num[i][j]:
      s.add(k)

print(s[K])
