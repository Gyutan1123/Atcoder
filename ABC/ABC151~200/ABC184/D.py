import sys
import collections, heapq, string, math, itertools, copy, bisect, functools
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

a,b,c = MI()

d = collections.defaultdict(int)

def dp(a,b,c):
  if (a,b,c) in d:
    return d[(a,b,c)]
  if a >= 100 or b >= 100 or c >= 100:
    return 0
  
  d[(a,b,c)] = a/(a+b+c)*(1+dp(a+1,b,c)) + \
          b/(a+b+c)*(1+dp(a,b+1,c)) + \
          c/(a+b+c)*(1+dp(a,b,c+1))
  
  return d[(a,b,c)]


dp(a,b,c) 
print(d[(a,b,c)]) 
