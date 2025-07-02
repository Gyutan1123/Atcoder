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

n,a,b = MI()
p,q,r,s = MI()

ans = [['.']*(s-r+1) for _ in range(q-p+1)]

for i in range(q-p+1):
  for j in range(s-r+1):
    ii = i+p
    jj = j+r
    
    k1 = ii-a
    k2 = jj-b
    
    if (k1 == k2 and max(1-a,1-b) <= k1 <= min(n-a,n-b)) or \
       (k1 == -k2 and max(1-a,b-n) <= k1 <= min(n-a,b-1)):
      ans[i][j] = '#'
    

for a in ans:
  print(''.join(a))
