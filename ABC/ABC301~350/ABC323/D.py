import sys
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

import collections
import heapq

n = II()
S = [LI() for _ in range(n)]

que = []

d = collections.defaultdict(int)
for s,c in S:
  heapq.heappush(que, s)
  d[s] += c

ans = 0
while que:
  s = heapq.heappop(que)
  c = d[s]
  ans += c%2
  d[s] = c%2
  if c >= 2:
    t = 2*s
    if t not in d:
      heapq.heappush(que, t)
    d[t] += c//2

print(ans)