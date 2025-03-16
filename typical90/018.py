import sys
import collections, heapq, string, math
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

mod = 10**9 + 7
########################################################

t = II()
l,x,y = MI()

q = II()

w = 2*math.pi / t

for _ in range(q):
  e = II()
  y_t = -0.5*l*math.sin(w*e)
  z_t = 0.5*l*(1-math.cos(w*e))

  print(math.degrees(math.acos(
    math.sqrt(x**2 + (y-y_t)**2) /
    math.sqrt(x**2 + (y-y_t)**2 + z_t**2)
  )))
