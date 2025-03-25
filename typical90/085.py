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

k = II()

ans = 0

a = 1
while a**3 <= k:
  if k % a != 0:
    a += 1
    continue
  k2 = k//a
  b = 1
  while b**2 <= k2:
    if k2%b == 0 and a <= b and b <= k2//b:
      ans += 1
    b += 1
  a += 1
  
print(ans)