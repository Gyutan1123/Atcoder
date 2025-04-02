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

n,d = MI()
kabe = [tuple(MI()) for _ in range(n)]
kabe.sort()
left = 0
ans = 0
while left < n:
  r = kabe[left][1]
  right = left
  while (right < n-1 and kabe[right+1][0]-r+1 <= d):
    if kabe[right+1][1] < r:
      r = kabe[right+1][1]
    right += 1
  ans += 1  
  left = right+1
  
print(ans)