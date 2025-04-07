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
S = SI()
w = LI()

# 座標圧縮
# https://drken1215.hatenablog.com/entry/2021/08/09/235400

C = sorted(set(w))
D = { v: i for i, v in enumerate(C)}

child = []
adult = []

for i in range(n):
  if S[i] == '0':
    child.append(D[w[i]])
  else:
    adult.append(D[w[i]])

child.sort()
adult.sort()

ans = 0
  
for x in D.values():
  ans = max(ans,bisect.bisect_left(child,x)+(len(adult)-bisect.bisect_left(adult,x)))
  ans = max(ans,bisect.bisect_right(child,x)+(len(adult)-bisect.bisect_right(adult,x)))

print(ans)