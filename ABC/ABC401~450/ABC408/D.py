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
t = II()
for _ in range(t):
  n = II()
  S = SI()
  
  oneNum = S.count('1')
  
  tmp = 0
  Min = 0
  for s in S:
    if s == '0':
      tmp += 1
    else:
      tmp -= 1
    
    if tmp < Min:
      Min = tmp
    if tmp > 0:
      tmp = 0
  
  ans = oneNum + Min
  print(ans)
