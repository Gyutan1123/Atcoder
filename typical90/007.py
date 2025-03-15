import sys
import collections, heapq, string
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################

n = II()
A = LI()
q = II()

A.sort()

for _ in range(q):
  b = II()
  
  l = 0
  r = n-1
  while r-l > 1:
    mid = (l+r) // 2
    if A[mid] > b:
      r = mid
    else:
      l = mid
  
  print(min(abs(A[l]-b),abs(A[r]-b)))