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

ans = 0
s = set()

d1 = collections.defaultdict(int)
d2 = collections.defaultdict(int)

A = []
for i in range(n):
  m = II()
  tmp = []
  for j in range(m):
    p,e = MI()
    if d1[p] < e:
      d1[p] = e
      d2[p] = 1
    elif d1[p] == e:
      d2[p] += 1  
    tmp.append([p,e])
  A.append(tmp)
  
for i in range(n):
  m = len(A[i])
  dis = []
  for j in range(m):
    p,e = A[i][j]
    if d1[p] == e and d2[p] == 1:
      dis.append(p)
      
  if not tuple(dis) in s:
    ans += 1
    s.add(tuple(dis))
    
print(ans)