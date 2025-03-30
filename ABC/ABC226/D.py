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
n = II()

city = [LI() for _ in range(n)]
mahou = set()

for i in range(n):
  for j in range(n):
    if i == j:
      continue
    
    dx = city[i][0] - city[j][0]
    dy = city[i][1] - city[j][1]
    
    gcd = math.gcd(abs(dx),abs(dy))
    if (dx//gcd, dy//gcd) not in mahou:
      mahou.add((dx//gcd, dy//gcd))
      
print(len(mahou))