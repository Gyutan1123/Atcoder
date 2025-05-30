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
C = LI()
boxId = [i for i in range(n)]
box = [set() for _ in range(n)]
for i in range(n):
  box[i].add(C[i])

for _ in range(q):
  a,b = MI()
  a -= 1
  b -= 1
  if len(box[boxId[a]]) > len(box[boxId[b]]):
    boxId[a], boxId[b] = boxId[b], boxId[a]
  
  for c in box[boxId[a]]:
    box[boxId[b]].add(c)

  box[boxId[a]] = set()
  print(len(box[boxId[b]]))
