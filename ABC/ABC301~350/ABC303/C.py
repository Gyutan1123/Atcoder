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

n,m,h,k = MI()
s = SI()

P = set([tuple(LI()) for _ in range(m)])

now = [0, 0]

for i in range(n):
    if s[i] == "U":
        now[1] += 1
    elif s[i] == "D":
        now[1] -= 1
    elif s[i] == "L":
        now[0] -= 1
    else:
        now[0] += 1
    h -= 1
    if h < 0:
        print('No')
        exit()

    if tuple(now) in P and h < k:
        h = k
        P.remove(tuple(now))
  
print('Yes')
