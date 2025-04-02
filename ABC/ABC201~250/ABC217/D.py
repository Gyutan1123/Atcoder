import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################
l,q = MI()

S = SortedList([0,l])


for _ in range(q):
  c,x = MI()
  if c == 1:
    S.add(x)
  if c == 2:
    r = S.bisect_right(x)
    print(S[r]-S[r-1])