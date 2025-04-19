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

n,m = MI()


d = collections.defaultdict(set)
K = []
for i in range(m):
  I = LI()
  k = I[0]
  A = I[1:]
  for a in A:
    d[a].add(i)
  K.append(k)
  
  
B = LI()

ans = 0

for b in B:
  for i in d[b]:
    K[i] -= 1
    if K[i] == 0:
      ans += 1
    
  print(ans)