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

l,n1,n2 = MI()

x1 = []
x2 = []
now = 0
for i in range(n1):
  a,b = MI()
  x1.append((a, now, now+b))
  now += b
now = 0
for i in range(n2):
  a,b = MI()
  x2.append((a, now, now+b))
  now += b
  
i = 0

run1 = 0
run2 = 0

ans = 0
while run1 < n1 and run2 < n2:
  if x1[run1][0] == x2[run2][0]:
    end1 = x1[run1][2]
    end2 = x2[run2][2]
    
    if end1 < end2:
      ans += end1-i
      i = end1
      run1 += 1
    elif end1 > end2:
      ans += end2-i
      i = end2
      run2 += 1
    else:
      ans += end1-i
      i = end1
      run1 += 1
      run2 += 1
  else:
    end1 = x1[run1][2]
    end2 = x2[run2][2]
    if end1 < end2:
      i = end1
      run1 += 1
    elif end1 > end2:
      i = end2
      run2 += 1
    else:
      i = end1
      run1 += 1
      run2 += 1
    
print(ans)
