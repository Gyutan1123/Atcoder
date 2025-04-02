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

t = II()

for _ in range(t):
  a,s = MI()
  
  tmp = ['0']*(60)
  free = set()
  for i in range(60):
    if (a >> i) & 1:
      tmp[-i-1] = '1' 
    else:
      free.add(i)
      
  ds = s-int(''.join(tmp), 2)*2
  if ds < 0:
    print('No')
    continue
  
  flag = True
  for i in range(60):
    if (ds >> i) & 1:
      if i not in free:
        flag = False
        
  if flag:
    print('Yes')
  else:
    print('No')