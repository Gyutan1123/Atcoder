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

n,q = MI()
s = set()
for i in range(1,n+1):
  s.add(i)
  
connect = [set() for _ in range(n+1)]

for _ in range(q):
  query = LI()
  if query[0] == 1:
    u,v = query[1:]
    connect[u].add(v)
    connect[v].add(u)
    
    if u in s:
      s.discard(u)
    if v in s:
      s.discard(v)
  
  if query[0] == 2:
    v = query[1]
    for u in connect[v]:
      connect[u].discard(v)
      if len(connect[u]) == 0:
        s.add(u)
    
    connect[v] = set()
    s.add(v)
    
  
  print(len(s))