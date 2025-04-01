import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

x = II()
n = len(str(x))

D = SortedSet()

for i in range(10):
  for j in range(1,10):
    if (10-i)%j == 0:
      l = (10-i)//j
    else:
      l = 1 + (10-i)//j
    tmp = [0]*(l)
    tmp[-1] = str(i)
    if i != 0:
      D.add(i)
    for k in range(2,l+1):
      tmp[-k] = str(int(tmp[-k+1]) + j)
      D.add(int(''.join(tmp[-k:])))

    if i%j == 0:
      l = i//j
    else:
      l = 1+i//j

    tmp = [0]*(l)
    if l > 0:
      tmp[-1] = str(i)
      if i != 0:
        D.add(i)
      for k in range(2,l+1):
        tmp[-k] = str(int(tmp[-k+1]) - j)
        D.add(int(''.join(tmp[-k:])))
    

for i in range(1,10):
  tmp = f'{i}'*n
  D.add(int(tmp))
print(D[D.bisect_left(x)])