import sys
import collections, heapq, string, math, itertools, copy
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

n,m = MI()

A = LI()
B = LI()
C = LI()
D = LI()

choco = [(A[i],B[i]) for i in range(n)]
hako = [(C[i],D[i]) for i in range(m)]

choco.sort(reverse=True)
hako.sort(reverse=True)

s = SortedList()

j = 0
for i in range(n):
  a,b = choco[i]
  
  while j < m and hako[j][0] >= a:
    c,d = hako[j]
    s.add(d)
    j += 1
    
  k = s.bisect_left(b)
  if k != len(s):
    s.discard(s[k])
  else:
    print('No')
    exit()
    
print('Yes')