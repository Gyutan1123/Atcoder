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

n,x,y = MI()
B = [LI() for _ in range(n-1)]

T = [0]*(840)

for i in range(840):
  now = i
  for j in range(n-1):
    p,t = B[j]
    if now%p != 0:
      now += ((now//p)+1)*p - now
    now += t
  T[i] = now-i
  
q = II()
for _ in range(q):
  q = II()
  print(q+x+y+T[(q+x)%840])
