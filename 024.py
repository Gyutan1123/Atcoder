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

n,k = MI()
A = LI()
B = LI()

changeNum = sum(list(map(abs, [A[i]-B[i] for i in range(n)])))

if changeNum <= k and (changeNum - k) % 2 == 0:
  print('Yes')
else:
  print('No')