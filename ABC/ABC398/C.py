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

n = II()
A = LI()
Ac = A.copy()
S = [set() for _ in range(n+1)]

if n == 1:
  print(1)
  exit()
  

A.sort()

MAX = -1
for i in range(n):
  if i == 0:
    if A[0] != A[1]:
      MAX = A[0]
  elif i == n-1:
    if A[n-1] != A[n-2]:
      MAX = A[n-1]
  else:
    if A[i] != A[i-1] and A[i] != A[i+1]:
      MAX = A[i]
      
if MAX != -1:
  print(Ac.index(MAX)+1)
else:
  print(-1)