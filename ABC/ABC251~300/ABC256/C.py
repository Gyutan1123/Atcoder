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

h1,h2,h3,w1,w2,w3 = MI()


# ijm
# kln
# opq

ans = 0

for i in range(1,29):
  for j in range(1,29):
    for k in range(1,29):
      for l in range(1,29):
        m = h1-(i+j)
        n = h2-(k+l)
        o = w1-(i+k)
        p = w2-(j+l)
        if (m > 0 and n > 0 and o > 0 and p > 0
            and w3-(m+n) > 0 and w3-(m+n) == h3-(o+p)):
          ans += 1

print(ans)
