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

n = II()
S = SI()

d = collections.Counter(S)

ans = 0

i = 0
while i*i < 10**13:
  square = str(i*i)
  if len(square) > n:
    break
  square = square.zfill(n)
  ds = collections.Counter(square)
  flag = True
    
  for j in range(10):

    if d[str(j)] != ds[str(j)]:
      flag = False
      break
  if flag:
    ans += 1
  
  i += 1

print(ans)
