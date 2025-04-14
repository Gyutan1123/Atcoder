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

s = [SI() for _ in range(9)]
ans = 0
counted = set()
for i in range(9):
  for j in range(9):
    if s[i][j] != '#':
      continue
    for k in range(9):
      for l in range(9):
        if s[k][l] != "#":
          continue
        dx = i-k
        dy = j-l
        if dx==0 and dy==0:
          continue

        if ((0 <= i+dy < 9 and 0 <= j-dx < 9 
            and 0 <= k+dy < 9 and 0 <= l-dx < 9) 
            and s[i+dy][j-dx] == "#" and s[k+dy][l-dx] == "#"):
          
          sq = [(i,j),(k,l),(i+dy,j-dx),(k+dy,l-dx)]
          sq =tuple(sorted(sq))
          if not sq in counted:
            ans += 1
            counted.add(sq)
        
        dx *= -1
        dy *= -1

        if ((0 <= i+dy < 9 and 0 <= j-dx < 9 
            and 0 <= k+dy < 9 and 0 <= l-dx < 9) 
            and s[i+dy][j-dx] == "#" and s[k+dy][l-dx] == "#"):
          
          sq = [(i,j),(k,l),(i+dy,j-dx),(k+dy,l-dx)]
          sq =tuple(sorted(sq))
          if not sq in counted:
            ans += 1
            counted.add(sq)
          
print(ans)