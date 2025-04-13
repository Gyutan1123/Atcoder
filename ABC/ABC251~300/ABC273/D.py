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

h,w,rs,cs = MI()
n = II()

kabeR = collections.defaultdict(SortedList)
kabeC = collections.defaultdict(SortedList)
for _ in range(n):
  r,c = MI()
  kabeR[r].add(c)
  kabeC[c].add(r)
  
nowr = rs
nowc = cs

q = II()
for _ in range(q):
  d,l = list(input().split())
  l = int(l)
  
  if d == 'L':
    i = kabeR[nowr].bisect_left(nowc)
    if i > 0:
      nowc = max(1,nowc-l,kabeR[nowr][i-1]+1)
    else:
      nowc = max(1,nowc-l)
  
  if d == 'R':
    i = kabeR[nowr].bisect_left(nowc)
    if i < len(kabeR[nowr]):
      nowc = min(w,nowc+l,kabeR[nowr][i]-1)
    else:
      nowc = min(w,nowc+l)

  if d == 'U':
    i = kabeC[nowc].bisect_left(nowr)
    if i > 0:
      nowr = max(1,nowr-l,kabeC[nowc][i-1]+1)
    else:
      nowr = max(1,nowr-l)
      
  if d == 'D':
    i = kabeC[nowc].bisect_left(nowr)
    if i < len(kabeC[nowc]):
      nowr = min(h,nowr+l,kabeC[nowc][i]-1)
    else:
      nowr = min(h,nowr+l)
  
  print(nowr,nowc)