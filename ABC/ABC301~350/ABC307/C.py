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

ha,wa = MI()
A = [SI() for _ in range(ha)]

maxh = 0
maxw = 0
minh = ha
minw = wa
for i in range(ha):
  for j in range(wa):
    if A[i][j] == '#':
      maxh = max(maxh,i+1)
      maxw = max(maxw,j+1)
      minh = min(minh,i+1)
      minw = min(minw,j+1)
ha = maxh - minh + 1
wa = maxw - minw + 1
A = [A[i][minw-1:maxw] for i in range(minh-1,maxh)]

hb,wb = MI()
B = [SI() for _ in range(hb)]
maxh = 0
maxw = 0
minh = hb
minw = wb
for i in range(hb):
  for j in range(wb):
    if B[i][j] == '#':
      maxh = max(maxh,i+1)
      maxw = max(maxw,j+1)
      minh = min(minh,i+1)
      minw = min(minw,j+1)
hb = maxh - minh + 1
wb = maxw - minw + 1
B = [B[i][minw-1:maxw] for i in range(minh-1,maxh)]

hx,wx = MI()
X = [SI() for _ in range(hx)]
maxh = 0
maxw = 0
minh = hx 
minw = wx
for i in range(hx):
  for j in range(wx):
    if X[i][j] == '#':
      maxh = max(maxh,i+1)
      maxw = max(maxw,j+1)
      minh = min(minh,i+1)
      minw = min(minw,j+1)
       
hx = maxh - minh + 1
wx = maxw - minw + 1
X = [X[i][minw-1:maxw] for i in range(minh-1,maxh)]

if max(ha,hb) > hx or max(wa,wb) > wx:
  print('No')
  exit()


for i in range(wx-wa+1):
  for j in range(hx-ha+1):
    for k in range(wx-wb+1):
      for l in range(hx-hb+1):
        C = [['.']*wx for _ in range(hx)]
        for m in range(ha):
          for n in range(wa):
            if A[m][n] == '#':
              C[j+m][i+n] = '#'
              
        for m in range(hb):
          for n in range(wb):
            if B[m][n] == '#':
              C[l+m][k+n] = '#'

        flag = True
        for m in range(hx):
          for n in range(wx):
            if C[m][n] != X[m][n]:
              flag = False
              break
      
        if flag:
          print('Yes')
          exit()
print('No')
