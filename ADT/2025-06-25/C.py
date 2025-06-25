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

s = list(SI())

cnt = 0
if s[0] == 'o':
  s.insert(0,'i')
  cnt += 1
if s[-1] == 'i':
  s.append('o')
  cnt += 1
  
while True:
  flag = False
  for i in range(len(s)-1):
    if s[i] == 'i' and s[i+1] == 'i':
      s.insert(i+1, 'o')
      cnt += 1
      flag = True
      break
    if s[i] == 'o' and s[i+1] == 'o':
      s.insert(i+1, 'i')
      cnt += 1
      flag = True
      break
  
  if not flag:
    break
  
print(cnt)
