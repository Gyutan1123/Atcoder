import sys
import collections, heapq, string, math, itertools

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n,m = MI()
connect = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = MI()
  connect[a].append(b)
  connect[b].append(a)
  
ans = 0
for i in range(1,n+1):
  connect[i].sort()
  if len(connect[i]) == 1 and connect[i][0] < i:
    ans += 1
  
  elif len(connect[i]) >= 2 and connect[i][0] < i and connect[i][1] > i:
    ans += 1
  
print(ans)