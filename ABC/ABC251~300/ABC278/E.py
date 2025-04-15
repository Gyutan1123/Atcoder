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

H,W,N,h,w = MI()

A = [LI() for _ in range(H)]

S = [[[0]*(W+1) for _ in range(H+1)] for _ in range(N+1)]

for i in range(H):
  for j in range(W):
    S[A[i][j]][i+1][j+1] += 1
    
for k in range(N+1):
  for i in range(H+1):
    for j in range(W):
      S[k][i][j+1] += S[k][i][j]
  for j in range(W+1):
    for i in range(H):
      S[k][i+1][j] += S[k][i][j]


ans = [[0]*(W-w+1) for _ in range(H-h+1)]

for k in range(H-h+1):
  for l in range(W-w+1):
    types = N
    for n in range(1,N+1):
      if S[n][H][W] - (S[n][k+h][l+w]-S[n][k][l+w]-S[n][k+h][l]+S[n][k][l]) == 0:
        types -= 1
    
    ans[k][l] = types
    
for a in ans:
  print(*a)