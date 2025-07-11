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
s = SI()

ans = float('inf')

for shift in range(n):
  tmp = s[shift:]+s[:shift]
  cost = shift*a
  
  for i in range(n//2):
    if tmp[i] != tmp[n-1-i]:
      cost += b
  
  ans = min(ans, cost)
  
print(ans)