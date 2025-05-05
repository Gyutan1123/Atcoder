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

def carpet(k):
  if k == 0:
    return [['#']]
  else:
    ret = [['.']*3**k for _ in range(3**k)]
    c = carpet(k-1)
    for i in range(3**(k-1)):
      for j in range(3**(k-1)):
        ret[i][j] = c[i][j]
        ret[i][j+3**(k-1)] = c[i][j]
        ret[i][j+2*3**(k-1)] = c[i][j]
        ret[i+3**(k-1)][j] = c[i][j]
        ret[i+2*3**(k-1)][j] = c[i][j]
        ret[i+3**(k-1)][j+2*3**(k-1)] = c[i][j]
        ret[i+2*3**(k-1)][j+3**(k-1)] = c[i][j]
        ret[i+2*3**(k-1)][j+2*3**(k-1)] = c[i][j]
        
    return ret  

for c in carpet(II()):
  print(''.join(c))