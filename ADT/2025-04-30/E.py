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
A = LI()
B = LI()

da = dict()
db = dict()

for i in range(n):
  da[A[i]] = i
for i in range(m):
  db[B[i]] = i

C = A + B
C.sort()

ansA = [0]*(n)
ansB = [0]*(m)

for i in range(n+m):
  if C[i] in da:
    ansA[da[C[i]]] = i+1
  else:
    ansB[db[C[i]]] = i+1

print(*ansA)
print(*ansB)