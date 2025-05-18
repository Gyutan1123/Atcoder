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

def sum1toN(n):
  return n*(n+1)//2

n,k = MI()
A = LI()

A.append(0)
A.sort(reverse=True)

ans = 0
for i in range(n):
  cnt = (i+1)*(A[i]-A[i+1])
  if k >= cnt:
    k -= cnt
    ans += (i+1)*(sum1toN(A[i])-sum1toN(A[i+1]))
  elif k > 0:
    x = k//(i+1)
    y = k%(i+1)
    ans += (i+1)*(sum1toN(A[i])-sum1toN(A[i]-x))
    ans += y*(A[i]-x)
    break

print(ans)