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

s = SI()
t = SI()

i = 0
while i < len(t):
  if s[i] != '?' and t[i] != '?' and s[i] != t[i]:
    break
  i += 1
p = i

i = 0
while i < len(t):
  if s[-1-i] != '?' and t[-1-i] != '?' and s[-1-i] != t[-1-i]:
    break  
  i += 1
q = i

for x in range(len(t)+1):
  if len(t)-q <= x <= p:
    print('Yes')
  else:
    print('No')