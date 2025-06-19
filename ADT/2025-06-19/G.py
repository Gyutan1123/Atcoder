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

slime = [LI() for _ in range(n)]

cnt = collections.defaultdict(int)
for s,c in slime:
  cnt[s] += c
heap = []
for s in cnt:
  heapq.heappush(heap, s)

ans = 0

while heap:
  s = heapq.heappop(heap)
  c = cnt[s]
  if c%2 == 1:
    ans += 1
    cnt[s] -= 1
  
  if cnt[s] > 0:
    if s*2 not in cnt:
      heapq.heappush(heap, s*2)
    cnt[s*2] += cnt[s]//2
  
  cnt[s] = 0

print(ans)