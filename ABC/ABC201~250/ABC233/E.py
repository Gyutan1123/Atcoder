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
x = list(SI())
s = [0]
n = len(x)
ans = [0]*(10*n)
for i in range(n):
  s.append(s[-1]+int(x[i]))

i = 0
c = 0
tmp = 0
while True:
  i += 1
  if i <= n:
    tmp += s[-i]
  
  ans[-i] = str(tmp%10)
  tmp //= 10

  if tmp == 0 and i >= n:
    break
  
print(''.join(ans[-i:]))