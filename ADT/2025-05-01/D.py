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
n = II()

A = [LI() for _ in range(n)]
B = [LI() for _ in range(n)]

# 行列の90度回転
# https://qiita.com/rudorufu1981/items/5341d9603ecb1f9c2e5c

zukei0 = A
zukei1 = []
zukei2 = []
zukei3 = []
for s in zip(*zukei0[::-1]):
  zukei1.append(list(s))
for s in zip(*zukei1[::-1]):
  zukei2.append(list(s))
for s in zip(*zukei2[::-1]):
  zukei3.append(list(s))

flag = True
for i in range(n):
  for j in range(n):
    if zukei0[i][j] == 1 and B[i][j] == 0:
      flag = False
      break

if flag:
  print("Yes")
  exit()

flag = True
for i in range(n):
  for j in range(n):
    if zukei1[i][j] == 1 and B[i][j] == 0:
      flag = False
      break

if flag:
  print("Yes")
  exit()


flag = True
for i in range(n):
  for j in range(n):
    if zukei2[i][j] == 1 and B[i][j] == 0:
      flag = False
      break

if flag:
  print("Yes")
  exit()

flag = True
for i in range(n):
  for j in range(n):
    if zukei3[i][j] == 1 and B[i][j] == 0:
      flag = False
      break

if flag:
  print("Yes")
  exit()

print("No")