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
n = II()

tmp = 0
for i in range(len(s)):
  if s[-1-i] == '1':
    tmp += 1<<i

if tmp > n:
  print(-1)
  exit()

for i in range(len(s)):
  if s[i] == '?':
    if tmp+(1<<(len(s)-1-i)) <= n:
      tmp += 1<<(len(s)-1-i)
  
print(tmp)