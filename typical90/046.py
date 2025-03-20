import sys
import collections, heapq, string, math, itertools

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n = II()
A = LI()
B = LI()
C = LI()
d_A = collections.defaultdict(int)
d_B = collections.defaultdict(int)
d_C = collections.defaultdict(int)
for i in range(n):
  d_A[A[i]%46] += 1
  d_B[B[i]%46] += 1
  d_C[C[i]%46] += 1
  
ans = 0
for i in range(46):
  for j in range(46):
    k = (46-i-j)%46
    ans += d_A[i]*d_B[j]*d_C[k]
  
print(ans)