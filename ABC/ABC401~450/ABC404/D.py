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

n,m = MI()
C = LI()

A = [LI() for _ in range(m)]
B = [[] for _ in range(n)]
for i in range(m):
  for a in A[i][1:]:
    B[a-1].append(i)


ans = float('inf')

for i in range(3**n):
  tmp = 0
  count = [0]*m
  now = i  
  for j in range(n):
    if now%3 == 1:
      tmp += C[j]
      for a in B[j]:
        count[a] += 1
    elif now%3 == 2:
      tmp += 2*C[j]
      for a in B[j]:
        count[a] += 2
    now //= 3
    
  flag = True
  for j in range(m):
    if count[j] < 2:
      flag = False
      break
  
  if flag:
    ans = min(ans, tmp)
    
print(ans)
