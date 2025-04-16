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

n,m,k = MI()
A = LI()

ans = []

s = SortedList()
tmp = 0
for i in range(m):
  s.add(A[i])
for i in range(k):
  tmp += s[i]

ans.append(tmp)
for i in range(n-m):
  if s.bisect_left(A[i]) < k:
    tmp -= A[i]
    if len(s) > k:
      tmp += s[k]
  s.discard(A[i])
  
  if s.bisect_right(A[i+m]) < k:
    if len(s) > k:
      tmp -= s[k-1]
    tmp += A[i+m]
  s.add(A[i+m])
  
  ans.append(tmp)
  
print(*ans)