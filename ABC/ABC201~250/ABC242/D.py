import sys
import collections, heapq, string, math, itertools, copy
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

s = SI()
q = II()

A = 'ABC'
S = []
for i in range(len(s)):
  if s[i] == 'A':
    S.append(0)
  if s[i] == 'B':
    S.append(1)
  if s[i] == 'C':
    S.append(2)

def f(t,k):
  if t == 0:
    return S[k]
  elif k == 0:
    return (S[0]+t)%3
  else:
    if k%2 == 0:
      return (f(t-1,k//2)+1)%3
    if k%2 == 1:
      return (f(t-1,k//2)+2)%3
  

for _ in range(q):
  t,k = MI()
  print(A[f(t,k-1)])