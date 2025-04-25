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
mod = 998244353
########################################################

q = II()

num = 1
que = collections.deque()
que.append(1)

for _ in range(q):
  query = LI()
  if query[0] == 1:
    x = query[1]
    num = (10*num+x)%mod
    que.append(x)
  if query[0] == 2:
    x = que.popleft()
    num = (num-x*pow(10,len(que),mod))%mod

  if query[0] == 3:
    print(num%mod)