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

n,q = MI()

#ラベルiが貼ってある巣
su = [-1]*(n+1)
#巣iに貼ってあるラベル
label = [-1]*(n+1)
#鳩iがいる巣のラベル
hato = [-1]*(n+1)
for i in range(1, n+1):
  su[i] = i
  label[i] = i
  hato[i] = i
  
for i in range(q):
  op = LI()
  if op[0] == 1:
    a,b = op[1], op[2]
    hato[a] = label[b]

  if op[0] == 2:
    a,b = op[1], op[2]
    label[a], label[b] = label[b], label[a]
    su[label[a]] = a
    su[label[b]] = b

  if op[0] == 3:
    print(su[hato[op[1]]])