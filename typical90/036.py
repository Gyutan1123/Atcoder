import sys
import collections, heapq, string, math, itertools
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

mod = 10**9 + 7
########################################################

n,q = MI()
# 45度回転後の点
pd = []
xmax = -float('inf')
ymax = -float('inf')
xmin = float('inf')
ymin = float('inf')
for _ in range(n):
  x,y = MI()
  pd.append((x-y,x+y))
  xmax = max(xmax,x-y)
  xmin = min(xmin,x-y)
  ymax = max(ymax,x+y)
  ymin = min(ymin,x+y)
  
for _ in range(q):
  q = II()
  x,y = pd[q-1]
  print(max(max(abs(x-xmax),abs(x-xmin)),max(abs(y-ymax),abs(y-ymin))))