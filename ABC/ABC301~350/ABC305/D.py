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
A = LI()
q = II()

S = [0]
for i in range(1,n):
  if i%2 == 0:
    S.append(S[-1]+(A[i]-A[i-1]))
  else:
    S.append(S[-1])

for _ in range(q):
  l,r = MI()
  i = bisect.bisect_right(A,l)
  j = bisect.bisect_right(A,r)

  ans = 0
  if i%2 == 0:
    ans += A[i]-l
  if j%2 == 0:
    ans += r-A[j-1]

  ans += S[j-1]-S[i]
  
  print(ans)