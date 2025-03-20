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
n,p,q = MI()
A = LI()
ans = 0
for comb in itertools.combinations(range(n),5):
  tmp = 1
  for i in range(5):
    tmp *= A[comb[i]]
    tmp %= p
  if tmp % p == q:
    ans += 1
print(ans)  