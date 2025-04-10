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
P = LI()

ans = [0]*n

for i in range(n):
  p = P[i]
  ans[(p-i-1)%n] += 1
  ans[(p-i)%n] += 1
  ans[(p-i+1)%n] += 1
  
print(max(ans))
  