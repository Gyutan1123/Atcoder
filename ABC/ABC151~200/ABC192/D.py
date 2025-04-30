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
def base_10(num_n,n):
    """ n進数の数を10進数に変換

    Args:
        num_n (int): n新数の数
        n (int): 基数n
    Returns:
        int: num_nを10進数に変換した数
    """
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


X = SI()
M = II()

if len(X) == 1:
  if int(X) <= M:
    print(1)
  else:
    print(0)
  exit()

d = max(map(int, X))
if base_10(X, d+1) > M:
  print(0)
  exit()

l = d+1
r = 10**30
while r-l > 1:
  mid = (l+r)//2
  xmid = base_10(X, mid)
  if xmid <= M:
    l = mid
  else:
    r = mid

print(l-d)