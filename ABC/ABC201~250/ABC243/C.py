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

n = II()
XY = [LI() for _ in range(n)]
S = SI()
dl = collections.defaultdict(lambda:-1)
dr = collections.defaultdict(lambda:10**10)
for i in range(n):
  x,y = XY[i]
  s = S[i]
  if s == 'L':
    dl[y] = max(dl[y],x)
  if s == 'R':
    dr[y] = min(dr[y],x)
    
ans = 'No'
for i in range(n):
  x,y = XY[i]
  if dl[y] > dr[y]:
    ans = 'Yes'
print(ans)