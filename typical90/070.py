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

n = II()
X = []
Y = []
for _ in range(n):
  x,y = MI()
  X.append(x)
  Y.append(y)
  
X.sort()
Y.sort()

print(sum([abs(X[n//2]-X[i]) for i in range(n)]) 
      + sum([abs(Y[n//2]-Y[i]) for i in range(n)]))