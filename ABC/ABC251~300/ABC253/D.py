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

n,a,b = MI()

s = n*(n+1)//2

lcm = math.lcm(a,b)
s -= a*(n//a)*(n//a+1)//2
s -= b*(n//b)*(n//b+1)//2
s += lcm*(n//lcm)*(n//lcm+1)//2

print(s)