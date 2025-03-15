import sys
import collections, heapq, string

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

########################################################

n = II()

z = 1
while z**3 < n:
  if (n-z**3) % (3*z) != 0:
    z += 1
    continue 
  m = (n-z**3) // (3*z)
  l = 0
  r = n 

  while r - l > 1:
    mid = (r+l) // 2
    if pow(mid,2) + mid*z >= m:
      r = mid
    else:
      l = mid
    
    
  if pow(r,2) + r*z == m:
    print(r+z,r)
    exit()
  
  z += 1
      
print(-1)
