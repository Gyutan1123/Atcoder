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

# 行列の90度回転
# https://qiita.com/rudorufu1981/items/5341d9603ecb1f9c2e5c

zukei0 = [S[i][left:right+1] for i in range(bottom, top+1)]
zukei1 = []
zukei2 = []
zukei3 = []
for s in zip(*zukei0[::-1]):
  zukei1.append(list(s))
for s in zip(*zukei1[::-1]):
  zukei2.append(list(s))
for s in zip(*zukei2[::-1]):
  zukei3.append(list(s))

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