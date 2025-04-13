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
A = LI()

d = collections.defaultdict(set)

for i in range(n):
  l = -A[i]//(i+1)-1
  r = (n-A[i]-1)//(i+1) + 1
  for j in range(l,r+1):
    d[j].add(i)
    
for i in range(1,m+1):
  s = set()
  for j in d[i]:
    s.add(A[j]+(j+1)*i)
  
  for k in range(len(s)+1):
    if k not in s:
      print(k)
      break