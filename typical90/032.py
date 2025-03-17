import sys
import collections, heapq, string, math, itertools
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

mod = 10**9 + 7
########################################################

n = II()
A = [LI() for _ in range(n)]
m = II()
funaka = collections.defaultdict(set)
for _ in range(m):
  x,y = MI()
  funaka[x].add(y)
  funaka[y].add(x)

ans = 10**10

for p in itertools.permutations(range(1,n+1)):
  tmp = A[p[0]-1][0]
  for i in range(1,n):
    if p[i-1] in funaka[p[i]]:
      tmp += 10**11
    else:
      tmp += A[p[i]-1][i]
  
  ans = min(ans, tmp)
  
print(ans if ans < 10**10 else -1)
