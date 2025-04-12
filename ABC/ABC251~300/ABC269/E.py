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

n = II()

l = 1
r = n
while r-l > 0:
  mid = (r+l)//2
  print(f'? {l} {mid} 1 {n}', flush=True)
  t = II()

  if t == mid-l+1:
    l = mid+1
  else:
    r = mid

i = l

l = 1
r = n

while r-l > 0:
  mid = (r+l)//2
  print(f'?  1 {n} {l} {mid}', flush=True)
  t = II()

  if t == mid-l+1:
    l = mid+1
  else:
    r = mid

j = l
  
print(f'! {i} {j}')