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

n,q = MI()
A = LI()

# sortedListはSortedSetよりも速い
s = SortedList(range(n+1))

for a in A:
  if a in s:
    s.remove(a)
  
d = collections.Counter(A)
for i in range(q):
  i,x = MI()
  d[A[i-1]] -= 1
  if d[A[i-1]] == 0 and A[i-1] <= n:
    s.add(A[i-1])
    
  A[i-1] = x
  if d[x] == 0 and x <= n: 
    s.remove(x)
  d[x] += 1

  print(s[0])