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

a,b,C = MI()

n = 0
for i in range(60):
  if (C>>i)&1:
    n += 1

if ((a+b-n)%2 != 0 
    or (a-b+n)%2 != 0 
    or a+b-n < 0 
    or a-b+n < 0 
    or n < a-b
    or a+b+n > 120):
  print(-1)
  exit()

a0 = (a+b-n)//2
a1 = (a-b+n)//2

X = [0]*60
Y = [0]*60
for i in range(60):
  if (C>>i)&1:
    if a1 > 0:
      X[i] = 1
      a1 -= 1
    else:
      Y[i] = 1
  else:
    if a0 > 0:
      X[i] = 1
      Y[i] = 1
      a0 -= 1

X.reverse()
Y.reverse()
X = ''.join(map(str,X))
Y = ''.join(map(str,Y))
print(int(X,2), int(Y,2))