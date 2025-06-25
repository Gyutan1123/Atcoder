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

n,s = MI()
A = LI()

sf = [0]
for i in range(n):
  sf.append(sf[-1] + A[i])
  
df = collections.Counter(sf)

sb = [0]
for i in range(n):
  sb.append(sb[-1] + A[n-1-i])

db = collections.Counter(sb)

for i in df.keys():
  if s-i in db:
    print('Yes')
    exit()

      
dmodb = collections.defaultdict(SortedSet)

for i in db.keys():
  dmodb[i % sf[-1]].add(i)
  
for i in df.keys():
  if len(dmodb[(s-i)%sf[-1]]):
    j = dmodb[(s-i)%sf[-1]][-1]
    if s-i-j > 0:
      print('Yes')
      exit()

print('No')
