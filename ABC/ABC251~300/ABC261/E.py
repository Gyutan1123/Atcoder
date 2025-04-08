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

n,c = MI()

op = [LI() for _ in range(n)]

ans = [0]*(n)

for i in range(30):
  tmp = (c >> i) & 1
  f = [0,1]
  for j, (t,a) in enumerate(op):
    if t == 1:
      f = [f[0]&((a>>i)&1), f[1]&((a>>i)&1)]
    if t == 2:
      f = [f[0]|((a>>i)&1), f[1]|((a>>i)&1)]
    if t == 3:
      f = [f[0]^((a>>i)&1), f[1]^((a>>i)&1)]
      
    tmp = f[tmp]
    ans[j] += tmp << i
    
for i in range(n):
  print(ans[i])