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

l,r = MI()

logl = len(str(l))-1
logr = len(str(r))-1

if logl == logr:
  print(((logr+1)*(r*(r+1) - l*(l-1))//2) % mod)
else:
  ans = 0
  ans += (logl+1)*(10**(logl+1)*(10**(logl+1)-1)-l*(l-1))//2
  for i in range(logl+1,logr):
    ans += (i+1)*(10**(i+1)*(10**(i+1)-1)-10**i*(10**i-1))//2
  ans += (logr+1)*(r*(r+1)-10**logr*(10**logr-1))//2
  print(ans%mod) 