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

n,m,d = MI()
A = LI()
B = LI()
A.sort()
B.sort()

ans = -1
for a in A:
  l = bisect.bisect_left(B,a-d)
  r = bisect.bisect_right(B,a+d) 
  
  if l < r and l != len(B) and r != 0:
    ans = max(ans,a+B[r-1])
    
print(ans)