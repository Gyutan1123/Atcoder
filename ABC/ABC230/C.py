import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

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

ans = [["."]*(s-r+1) for _ in range(q-p+1)]

for i in range(q-p+1):
  for j in range(s-r+1):
    x = i+p
    y = j+r
    k = x-a
    if ((max(1-a,1-b) <= k and k <= min(n-a,n-b) and y == b+k )
        or max(1-a,b-n) <= k and k <= min(n-a,b-1) and y == b-k):
      ans[i][j] = '#'
      
      
for a in ans:
  print(''.join(a))