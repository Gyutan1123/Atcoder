import sys
import collections, heapq, string, math, itertools, copy
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

T = II()
for _ in range(T):
  n = II()
  A = LI()
  place = [[-1,-1] for _ in range(n+1)]
  for i in range(len(A)):
    if place[A[i]][0] != -1:
      place[A[i]][1] = i
    else:
      place[A[i]][0] = i
  
  ans = 0
  n *= 2
  checked = set()
  for a in A:
    if a in checked:
      continue
    checked.add(a)
    i1,i2 = place[a]
    
    if abs(i1-i2) == 1:
      continue
    
    if i1 == 0:
      Next = A[i1+1]
      if Next < a:
        continue
      
      if i2 == n-1:
        j1,j2 = place[A[i2-1]]
        if abs(j1-j2) != 1 and Next == A[i2-1] and i1+1 != i2-1:
          ans += 1
      else:
        j1,j2 = place[A[i2-1]]
        j3,j4 = place[A[i2+1]]
        if abs(j1-j2) != 1 and Next == A[i2-1] and i1+1 != i2-1:
          ans += 1
        elif abs(j3-j4) != 1 and Next == A[i2+1] and 1+1 != i2+1:
          ans += 1
      
    else:
      Next1 = A[i1+1]
      Next2 = A[i1-1]
      if i2 == n-1:
        j1,j2 = place[A[i2-1]]
        if abs(j1-j2) != 1 and Next1 == A[i2-1] and a < Next1 and i1+1 != i2-1:
          ans += 1
        elif abs(j1-j2) != 1 and Next2 == A[i2-1] and a < Next2 and i1-1 != i2-1:
          ans += 1
      else:
        j1,j2 = place[A[i2-1]]
        j3,j4 = place[A[i2+1]]
        
        if abs(j1-j2) != 1 and Next1 == A[i2-1] and a < Next1 and i1+1 != i2-1:
          ans += 1 
        elif abs(j3-j4) != 1 and Next1 == A[i2+1] and a < Next1 and i1+1 != i2+1:
          ans += 1
        if abs(j1-j2) != 1 and Next2 == A[i2-1] and a < Next2 and i1-1 != i2-1:
          ans += 1
        elif abs(j3-j4) != 1 and Next2 == A[i2+1] and a < Next2 and i1-1 != i2+1:
          ans += 1
        
  print(ans)