import sys
import collections, heapq

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################


h,w = MI()
A = [LI() for _ in range(h)]

sum_c_A = [0]*h
sum_r_A = [0]*w

for i in range(h):
  sum_c_A[i] = sum(A[i])
  
for j in range(w):
  sum_r_A[j] = sum([A[i][j] for i in range(h)])
  

B = [[0]*w for _ in range(h)]

for i in range(h):
  for j in range(w):
    B[i][j] = sum_c_A[i] + sum_r_A[j] - A[i][j]
    

for b in B:
  print(' '.join([str(b_item) for b_item in b]))