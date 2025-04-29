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

n,m = MI()
P = LI()

connect = [[] for _ in range(n+1)]
for i in range(n-1):
  p = P[i]
  connect[p].append(i+2)

h = [-1]*(n+1)

for _ in range(m):
  x,y = MI()
  if h[x] < y:
    h[x] = y
  
que = []

for i in range(1,n+1):
  heapq.heappush(que, (-h[i], i))

while que:
  _, now = heapq.heappop(que)
  for to in connect[now]:
    if h[to] < h[now] - 1:
      h[to] = h[now] - 1
      heapq.heappush(que, (-h[to], to))

ans = 0
for i in range(1,n+1):
  if h[i] >= 0:
    ans += 1

print(ans)