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

h,w = MI()
P = [LI() for _ in range(h)]

ans = 1

for hnum in range(1, h+1):
  for comb in itertools.combinations(range(h),hnum):
    d = collections.defaultdict(lambda:0)
    
    for j in range(w):
      s = set()
      for i in comb:
        s.add(P[i][j])
      if len(s) == 1:
        tmp = s.pop()
        d[tmp] += 1
        
    wnum = 0
    for p in range(1,h*w+1):
      wnum = max(d[p], wnum)
    ans = max(ans,hnum*wnum)
    
print(ans)        