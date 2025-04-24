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

n,k = MI()
A = LI()

que = [0]
k += 1
cnt = 0
s = set()
s.add(0)
while True:
  now = heapq.heappop(que)
  cnt += 1
  if cnt == k:
    print(now)
    break

  for a in A:
    if a+now not in s:
      s.add(a+now)
      heapq.heappush(que,now+a)