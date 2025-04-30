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

s1,s2 = list(SI())
t1,t2 = list(SI())

if s1 > s2:
  s1,s2 = s2,s1

if t1 > t2:
  t1,t2 = t2,t1

l = dict()
l[('A','B')] = 1
l[('A','C')] = 2
l[('A','D')] = 2
l[('A','E')] = 1
l[('B','C')] = 1
l[('B','D')] = 2
l[('B','E')] = 2
l[('C','D')] = 1
l[('C','E')] = 2
l[('D','E')] = 1


if s1 == s2:
  l1 = 0
else:
  l1 = l[(s1,s2)]

if t1 == t2: 
  l2 = 0
else:
  l2 = l[(t1,t2)]



if l1 == l2:
  print('Yes')
else:
  print('No')
