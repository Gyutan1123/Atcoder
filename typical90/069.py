import sys
import collections, heapq, string, math, itertools

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(LS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n,k = MI()


if n == 1:
  print(k % mod)
elif n == 2:
  print((k*(k-1))%mod)
else:
  print((k*(k-1)*pow(k-2, n-2, mod))%mod)
