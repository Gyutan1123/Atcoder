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

res = n
cnt = 0

heap = []
for a in A:
  heapq.heappush(heap,a)

while True:
  tmp = heapq.heappop(heap)
  now = tmp-cnt
  if now <= 0:
    res -= 1
    continue
  else:
    if res*now < k:
      k -= res*now
      cnt += now
      res -= 1
    else:
      tmpCnt = k//res
      k -= tmpCnt*res
      cnt += tmpCnt
      break

for i in range(n):
  A[i] = max(0,A[i]-cnt)

i = 0
while k > 0:
  if A[i] > 0:
    A[i] -= 1
    k -= 1
  i = (i+1)%n

print(*A)