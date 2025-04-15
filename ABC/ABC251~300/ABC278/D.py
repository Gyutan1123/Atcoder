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
A = LI()
q = II()

for i in range(n):
  A[i] = (A[i],-1)
  
changeall = (-1,-100)
for T in range(q):
  query = LI()
  if query[0] == 1:
    x = query[1]
    changeall = (x,T)
  if query[0] == 2:
    i,x = query[1:]
    i -= 1
    a,t = A[i]
    if changeall[1] < t:
      A[i] = (a+x,T)
    else:
      A[i] = (changeall[0]+x,T)
      
  if query[0] == 3:
    i = query[1]-1
    a,t = A[i]
    
    if changeall[1] < t:
      print(a)
    else:
      print(changeall[0])