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

P1 = [list(SI()) for _ in range(4)]
P2 = [list(SI()) for _ in range(4)]
P3 = [list(SI()) for _ in range(4)]

left1 = 3
right1 = 0
bottom1 = 3
top1 = 0
left2 = 3
right2 = 0 
bottom2 = 3
top2 = 0
left3 = 3
right3 = 0
bottom3 = 3
top3 = 0

for i in range(4):
  for j in range(4):
    if P1[i][j] == '#':
      top1 = max(top1, i)
      bottom1 = min(bottom1, i)
      right1 = max(right1, j)
      left1 = min(left1, j)
    if P2[i][j] == '#':
      top2 = max(top2, i)
      bottom2 = min(bottom2, i)
      right2 = max(right2, j)
      left2 = min(left2, j)
    if P3[i][j] == '#':
      top3 = max(top3, i)
      bottom3 = min(bottom3, i)
      right3 = max(right3, j)
      left3 = min(left3, j)

# 行列の90度回転
# https://qiita.com/rudorufu1981/items/5341d9603ecb1f9c2e5c
zukei10 = [P1[i][left1:right1+1] for i in range(bottom1, top1+1)]
zukei11 = []
zukei12 = []
zukei13 = []
for s in zip(*zukei10[::-1]):
  zukei11.append(list(s))
for s in zip(*zukei11[::-1]):
  zukei12.append(list(s))
for s in zip(*zukei12[::-1]):
  zukei13.append(list(s))

zukei20 = [P2[i][left2:right2+1] for i in range(bottom2, top2+1)]
zukei21 = []
zukei22 = []
zukei23 = []
for s in zip(*zukei20[::-1]):
  zukei21.append(list(s))
for s in zip(*zukei21[::-1]):
  zukei22.append(list(s))
for s in zip(*zukei22[::-1]):
  zukei23.append(list(s))
zukei30 = [P3[i][left3:right3+1] for i in range(bottom3, top3+1)]
zukei31 = []
zukei32 = []
zukei33 = []
for s in zip(*zukei30[::-1]):
  zukei31.append(list(s))
for s in zip(*zukei31[::-1]):
  zukei32.append(list(s))
for s in zip(*zukei32[::-1]):
  zukei33.append(list(s))

for rot in range(4**3):
  if rot%4 == 0:
    p1 = zukei10
  if rot%4 == 1:
    p1 = zukei11
  if rot%4 == 2:
    p1 = zukei12
  if rot%4 == 3:
    p1 = zukei13
  rot //= 4
  if rot%4 == 0:
    p2 = zukei20
  if rot%4 == 1:
    p2 = zukei21
  if rot%4 == 2:
    p2 = zukei22
  if rot%4 == 3:
    p2 = zukei23
  rot //= 4
  if rot%4 == 0:
    p3 = zukei30
  if rot%4 == 1:
    p3 = zukei31
  if rot%4 == 2:
    p3 = zukei32
  if rot%4 == 3:
    p3 = zukei33
  
  tmp = [[0]*4 for _ in range(4)]
  
  sh1 = len(p1)
  sw1 = len(p1[0])
  sh2 = len(p2)
  sw2 = len(p2[0])
  sh3 = len(p3)
  sw3 = len(p3[0])
  
  for p1i in range(4):
    for p1j in range(4):
      for p2i in range(4):
        for p2j in range(4):
          for p3i in range(4):
            for p3j in range(4):
              tmp = [[0]*4 for _ in range(4)]
              flag = True
              for i in range(sh1):
                for j in range(sw1):
                  if not (0 <= p1i+i < 4 and 0 <= p1j+j < 4) and p1[i][j] == '#':
                    flag = False
                  if 0 <= p1i+i < 4 and 0 <= p1j+j < 4 and p1[i][j] == '#':
                    tmp[p1i+i][p1j+j] += 1
              for i in range(sh2):
                for j in range(sw2):
                  if not (0 <= p2i+i < 4 and 0 <= p2j+j < 4) and p2[i][j] == '#':
                    flag = False
                  if 0 <= p2i+i < 4 and 0 <= p2j+j < 4 and p2[i][j] == '#':
                    tmp[p2i+i][p2j+j] += 1
              for i in range(sh3):
                for j in range(sw3):
                  if not (0 <= p3i+i < 4 and 0 <= p3j+j < 4) and p3[i][j] == '#':
                    flag = False
                  if 0 <= p3i+i < 4 and 0 <= p3j+j < 4 and p3[i][j] == '#':
                    tmp[p3i+i][p3j+j] += 1
              # すべてのマスが1になっているか確認
              for i in range(4):
                for j in range(4):
                  if tmp[i][j] != 1:
                    flag = False
                
              if flag:
                print('Yes')
                exit()
                
print('No')