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

n,m = MI()
A = LI()

B = []
S = [0]
for a in A:
  S.append(S[-1]+a)

tmp = 0
for i in range(m):
  tmp += (i+1)*A[i]
B.append(tmp)

for i in range(n-m):
  B.append(B[-1]-(S[i+m]-S[i])+A[i+m]*m)

print(max(B))