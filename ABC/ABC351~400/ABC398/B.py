import sys
import collections, heapq, string, math, itertools

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

A = LI()
ans = 'No'
for c in itertools.combinations(range(7),5):
  s = set()
  for i in c:
    s.add(A[i])
    
  if len(s) != 2:
    continue
  
  n1 = s.pop()
  n2 = s.pop()
  tmp1 = 0
  tmp2 = 0
  for i in c:
    if A[i] == n1:
      tmp1 += 1
    if A[i] == n2:
      tmp2 += 1
  if (tmp1 == 3 and tmp2 == 2) or (tmp1 == 2 and tmp2 == 3):
    ans = 'Yes'
    
print(ans)