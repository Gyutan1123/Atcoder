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

n,q = MI()
A = LI()
shifts = 0
for _ in range(q):
  t,x,y = MI()
  if t == 1:
    A[(x-1-shifts)%n],A[(y-1-shifts)%n] = A[(y-1-shifts)%n],A[(x-1-shifts)%n]
  
  if t == 2:
    shifts += 1
  
  if t == 3:
    print(A[(x-1-shifts)%n])