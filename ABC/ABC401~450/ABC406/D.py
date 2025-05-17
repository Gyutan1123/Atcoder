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

h,w,n = MI()

numH = [0]*h
numW = [0]*w

posH = [set() for _ in range(h)]
posW = [set() for _ in range(w)]

for i in range(n):
  x,y = MI()
  numH[x-1] += 1
  numW[y-1] += 1
  
  posH[x-1].add(y-1)
  posW[y-1].add(x-1)
  
q = II()
for _ in range(q):
  query = LI()
  if query[0] == 1:
    print(numH[query[1]-1])
    if len(posH[query[1]-1]) > 0:
      for j in posH[query[1]-1]:
        numW[j] -= 1
        posW[j].remove(query[1]-1)
    numH[query[1]-1] = 0
    posH[query[1]-1] = set()
  elif query[0] == 2:
    print(numW[query[1]-1])
    if len(posW[query[1]-1]) > 0:
      for j in posW[query[1]-1]:
        numH[j] -= 1
        posH[j].remove(query[1]-1)
    numW[query[1]-1] = 0
    posW[query[1]-1] = set()