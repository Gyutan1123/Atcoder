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

S = collections.defaultdict(int)
S[(1,1)] = 2
S[(1,2)] = 3
S[(2,1)] = 3
S[(2,2)] = 6
S[(3,1)] = 3
S[(3,2)] = 7
S[(4,1)] = 4
S[(4,2)] = 8

def s(a,b):
  ret = 0
  ret += S[(4,2)]*(a//4)*(b//2)
  ret += S[(4,b%2)]*(a//4)
  ret += S[(a%4,2)]*(b//2)
  ret += S[(a%4,b%2)]
  return ret


a,b,c,d = MI()

a += 10**9
b += 10**9
c += 10**9
d += 10**9

print(s(c,d)+s(a,b)-s(a,d)-s(c,b))