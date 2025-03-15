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
A = LI()

ans = [0]*(n-1)

ls = set()
rs = set()

for i in range(n-1):
  ls.add(A[i])
  rs.add(A[(n-1)-i])
  
  ans[i] += len(ls)
  ans[(n-2)-i] += len(rs)
  
print(max(ans))