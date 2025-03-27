import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

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

S = [list(SI()) for _ in range(n)]
T = [list(SI()) for _ in range(n)]

top = 0
bottom = n-1
right = 0
left = n-1

for i in range(n):
  for j in range(n):
    if S[i][j] == '#':
      top = max(top, i)
      bottom = min(bottom, i)
      right = max(right, j)
      left = min(left, j)

zukei0 = [S[i][left:right+1] for i in range(bottom, top+1)]

zukei1 = []
for s in zukei0:
  zukei1.append(s[::-1])
zukei1.reverse()

zukei2 = []
for s in list(zip(*zukei0)):
  zukei2.append(list(s))
zukei2.reverse()

zukei3 = []
for s in zukei2:
  zukei3.append(list(s[::-1]))
zukei3.reverse()

top = 0
bottom = n-1
right = 0
left = n-1

for i in range(n):
  for j in range(n):
    if T[i][j] == '#':
      top = max(top, i)
      bottom = min(bottom, i)
      right = max(right, j)
      left = min(left, j)

zukei = [T[i][left:right+1] for i in range(bottom, top+1)]
     
if zukei == zukei0 or zukei == zukei1 or zukei == zukei2 or zukei == zukei3:
  print('Yes')
else:
  print('No')