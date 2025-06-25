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

n,m = MI()
A = LI()
B = LI()
choco = [(a,b) for a,b in zip(A,B)]
choco.sort(reverse=True)
C = LI()
D = LI()
box = [(c,d) for c,d in zip(C,D)]
box.sort(reverse=True)

s = SortedList()

j = 0
for i in range(n):
  a,b = choco[i]
  while j < m and box[j][0] >= a:
    s.add(box[j][1])
    j += 1
  
  if len(s) == 0 or s[-1] < b:
    print('No')
    exit()
  
  l = s.bisect_left(b)
  if l == len(s):
    print('No')
    exit()
  
  s.remove(s[l])
  
print('Yes')
