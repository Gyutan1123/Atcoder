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

a,b = MI()


l = 0
r = 10**15

while r-l > 1:
  x = (r+l)//2
  if (1+x)*(x**2+2*x+1) > (a**2)/(4*b**2):
    r = x
  else:
    l = x
    
def f(x):
  return b*x + a/((1+x)**(0.5))

print(min(f(l),f(r)))