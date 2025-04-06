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

n = II()
a = LI()
b = LI()
q = II()


j = 0
sa = set()
sb = set()
sab = set()

I = []

for i in range(n):
  if a[i] in sab:
    I.append(I[-1])
  
  else:
    if a[i] in sb:
      sb.discard(a[i])
      sab.add(a[i])
    else:
      sa.add(a[i])
  
    while j < n and len(sa) > 0 and len(sb) == 0:
      if b[j] in sab:
        pass
      elif b[j] in sa:
        sa.discard(b[j])
        sab.add(b[j])
      else:
        sb.add(b[j])
      j += 1
    
    if len(sa):
      I.append((n,n))
    else:
      l = j-1 
      while j < n and b[j] in sab:
        j += 1
      I.append((l,j))

for _ in range(q):
  x, y = MI()
  x -= 1
  y -= 1
  print("Yes" if I[x][0] <= y < I[x][1] else "No")