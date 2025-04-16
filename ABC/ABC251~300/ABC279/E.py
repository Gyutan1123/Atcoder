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

n,m = MI()
A = LI()

pairs = []
pos = collections.defaultdict(int)

B = [j for j in range(1,n+1)]

for i in range(m):
  a = A[i]
  if B[a-1] == 1:
    pair = B[a]
  elif B[a] == 1:
    pair = B[a-1]
  else:
    pair = -1
  pairs.append(pair)
  B[a-1],B[a] = B[a],B[a-1]

for i in range(n):
  pos[B[i]] = i+1
  
pos[-1] = pos[1]

for i in range(m):
  pair = pairs[i]
  print(pos[pair])