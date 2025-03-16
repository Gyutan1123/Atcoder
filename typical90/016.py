import sys
import collections, heapq, string
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

mod = 10**9 + 7
########################################################

n = II()
A,B,C = MI()

ans = 10000

for a in range(10000):
  for b in range(10000-a):
    if n-A*a-B*b >= 0 and (n-A*a-B*b) % C == 0:
      c = (n-A*a-B*b) // C 
      ans = min(ans,a+b+c)
  
print(ans)
      