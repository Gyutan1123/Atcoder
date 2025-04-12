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

n = II()
isloggedin = False
ans = 0
for _ in range(n): 
  s = SI()
  if s == 'login':
    isloggedin = True
  
  if s == 'logout':
    isloggedin = False
    
  if s == 'private' and not isloggedin:
    ans += 1
    
print(ans)