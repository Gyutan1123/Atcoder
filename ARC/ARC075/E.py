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

n,k = MI()
A = []
for i in range(n):
  a = II()
  A.append(a)


S = [0]
for a in A:
  S.append(S[-1]+a)

B = []
for i in range(n+1):
  B.append(S[i]-k*i)
  
ans = 0

s = SortedList()

for i in range(n+1):
  ans += s.bisect_right(B[i])
  s.add(B[i])

print(ans)
