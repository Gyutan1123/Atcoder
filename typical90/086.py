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

n,q = MI()
C = [LI() for _ in range(q)]

ans = 1


for i in range(60):
  tmp = 0
  for a in range(2**n):
    la = list(map(int, list(format(a,f'0{n}b'))))
    flag = True
    for x,y,z,w in C:
      if not ((la[x-1] | la[y-1] | la[z-1]) == (w >> i & 1)):
        flag = False
    if flag:
      tmp += 1
  
  ans *= tmp
  
print(ans%mod)