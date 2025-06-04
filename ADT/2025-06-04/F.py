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

n,d,p = MI()
F = LI()

F.sort()

s = [0]
for i in range(n):
  s.append(s[-1] + F[i])

ans = float('inf')

for i in range(n+1):
  passNum = i*d
  cost = p*i+s[max(0,n-passNum)]
  
  ans = min(ans, cost)
print(ans)