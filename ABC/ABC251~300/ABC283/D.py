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

S = SI()

d = collections.defaultdict(int)

l = [[]]

for s in S:
  if s == '(':
    l.append([])
  elif s == ')':
    for a in l[-1]:
      d[a] -= 1
    l.pop()
  else:
    if d[s] > 0:
      print('No')
      exit()
    else:
      d[s] = 1
      l[-1].append(s)
      
print('Yes')