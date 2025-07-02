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

n,r,c = MI()
S = SI()

shift = (0,0)

s = set([(0,0)])

ans = ''

for i in range(n):
  if S[i] == 'N':
    shift = (shift[0]+1,shift[1])
  elif S[i] == 'W':
    shift = (shift[0],shift[1]+1)
  elif S[i] == 'S':
    shift = (shift[0]-1,shift[1])
  elif S[i] == 'E':
    shift = (shift[0],shift[1]-1)
  
  s.add(shift)
  
  if (r+shift[0],c+shift[1]) in s:
    ans += '1'
  else:
    ans += '0'
    
print(ans)
