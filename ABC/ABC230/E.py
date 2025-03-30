import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

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

i = 1
ans = 0
while i*i <= n:
  m = n//i
  ans += m*(n//m-n//(m+1))
  i += 1

while 1 < m:
  m -= 1
  ans += m*(n//m-n//(m+1))
  
print(ans)