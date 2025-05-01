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

n,x = MI()

T = [LI() for _ in range(n)]
H = [sum(t) for t in T]

l = 1
r = min(H)+1

while r-l > 1:
  mid = (l+r)//2
  flag = True
  A = [(max(0,mid-T[0][1]), T[0][0])]
  if not (A[-1][0] <= A[-1][1]):
    flag = False
  
  for i in range(1,n):
    A.append((max(0, A[-1][0]-x, mid-T[i][1]), min(mid, T[i][0], A[-1][1]+x)))    
    if not (A[-1][0] <= A[-1][1]):
      flag = False
      break
    
  if flag:
    l = mid
  else:
    r = mid

print(sum([H[i]-l for i in range(n)]))