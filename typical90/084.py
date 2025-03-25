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

n = II()
S = SI()

dpo = [-1]*(n+1)
dpx = [-1]*(n+1)

for i in range(n):
  dpo[i+1] = dpo[i]
  dpx[i+1] = dpx[i]
  if S[i] == 'o':
    dpo[i+1] = i
  if S[i] == 'x':
    dpx[i+1] = i
  
ans = 0

for i in range(n):
  if S[i] == 'o':
    ans += dpx[i] + 1
  if S[i] == 'x':
    ans += dpo[i] + 1

print(ans)