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

h,w = MI()
C = [list(SI()) for _ in range(h)]

numH = [[0]*26 for _ in range(h)]
numW = [[0]*26 for _ in range(w)]

for i in range(h):
  for j in range(w):
    numH[i][ord(C[i][j])-ord('a')] += 1
    numW[j][ord(C[i][j])-ord('a')] += 1
    
visH = [False]*h
visW = [False]*w

nowH = h
nowW = w
while nowH >= 2 and nowW >= 2:
  delH = []
  delW = []
  
  if nowW >= 2:
    for i in range(h):
      if visH[i]:
        continue
      cnt = 0
      for j in range(26):
        if numH[i][j] == 0:
          cnt += 1
      if cnt == 25:
        visH[i] = True
        delH.append(i)
  
  if nowH >= 2:
    for j in range(w):
      if visW[j]:
        continue
      cnt = 0
      for i in range(26):
        if numW[j][i] == 0:
          cnt += 1
      if cnt == 25:
        visW[j] = True
        delW.append(j)
        
  if len(delH) == 0 and len(delW) == 0:
    break
  
  for i in delH:
    nowH -= 1
    for j in range(w):
      if C[i][j] != '?':
        numW[j][ord(C[i][j])-ord('a')] -= 1
        numH[i][ord(C[i][j])-ord('a')] -= 1
        C[i][j] = '?'
  for j in delW:
    nowW -= 1
    for i in range(h):
      if C[i][j] != '?':
        numH[i][ord(C[i][j])-ord('a')] -= 1
        numW[j][ord(C[i][j])-ord('a')] -= 1
        C[i][j] = '?'
  
ans = 0
for i in range(h):
  for j in range(w):
    if visH[i] or visW[j]:
      continue
    ans += 1
  
print(ans)