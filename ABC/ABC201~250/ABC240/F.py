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

t = II()

for _ in range(t):
  n,m = MI() 
  b = 0
  a = 0
  ans = -float('inf')
  for i in range(n):
    x,y = MI()
    ans = max(ans,a+b+x)
    if x < 0 and b > 0:
      i = b//(-x)
      if i < y:
        ans = max(ans, a+b*i+x*i*(i+1)//2)
      
    a += b*y+x*y*(y+1)//2
    b += x*y
    ans = max(ans,a)
  
  print(ans)