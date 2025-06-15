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

n,q = MI()
X = LI()

ans = []

boxes = [0]*n
for i in range(q):
  if X[i] >= 1:
    boxes[X[i]-1] += 1
    ans.append(X[i])
  else:
    m = min(boxes)
    for j in range(n):
      if boxes[j] == m:
        ans.append(j+1)
        boxes[j] += 1
        break
  
print(*ans)