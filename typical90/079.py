import sys
import collections, heapq, string, math, itertools

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

h,w = MI()
A = [LI() for _ in range(h)]
B = [LI() for _ in range(h)]

for i in range(h):
  for j in range(w):
    A[i][j] -= B[i][j]
    
ans = 0

for i in range(h-1):
  for j in range(w-1):
    tmp = A[i][j]
    A[i][j] -= tmp
    A[i+1][j] -= tmp
    A[i][j+1] -= tmp
    A[i+1][j+1] -= tmp
    ans += abs(tmp)
    
flag = True
for i in range(h):
  for j in range(w):
    if A[i][j] != 0:
      flag = False
      
if flag:
  print('Yes')
  print(ans)
else:
  print('No')    