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

n = II()

LR = [LI() for _ in range(n)]
L = [l for l,r in LR]
R = [r for l,r in LR]

SL = [0]
SR = [0]
for i in range(n):
  SL.append(SL[-1]+L[i])
  SR.append(SR[-1]+R[i])

if not (sum(L) <= 0 and 0 <= sum(R)):
  print("No")
else:
  ans = []
  tmp = 0
  for i in range(n):
    l,r = LR[i]
    ans.append(max(-(SR[n]-SR[i+1]+tmp),l))
    tmp += ans[-1]
  print("Yes")
  print(*ans)

