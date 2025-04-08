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
P = LI()

pre = [-1]*(n+1)
ans = [-1]*(n+1)
pile = [-1]*(n+1)
yama = SortedList()

if k == 1:
  for i in range(n):
    ans[P[i]] = i+1
  for a in ans[1:]:
    print(a)
  exit()

for turn in range(n):
  x = P[turn]
  if len(yama) == 0:
      yama.add(x)
      pile[x] = 1
  else:
    i = yama.bisect_left(x)
    if i == len(yama):
      yama.add(x)
      pile[x] = 1
    else:
      top,p = yama[i], pile[yama[i]]
      yama.discard(top)
      pre[x] = top
      if p+1 == k:
        now = x
        ans[x] = turn+1
        while pre[now] != -1:
          now = pre[now]
          ans[now] = turn+1
      else:
        yama.add(x)
        pile[x] = p+1

for a in ans[1:]:
  print(a)