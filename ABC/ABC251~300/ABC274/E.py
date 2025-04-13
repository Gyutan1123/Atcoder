import sys
import collections, heapq, string, math, itertools, copy, bisect
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

def dist(a,b):
  return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

n,m = MI()

dp = [[float('inf')]*(n+m) for _ in range(1 << (n+m))]

pos = [LI() for _ in range(n+m)]


for i in range(n+m):
  dp[1<<i][i] = dist((0,0), pos[i])
  

for s in range(1,1 << (n+m)):
  speed = 1
  for j in range(m):
    if s >> (n+j) & 1:
      speed *= 2
  for now in range(n+m):
    if not (s >> now) & 1:
      continue
    for to in range(n+m):
      if (s >> to) & 1:
        continue

      dp[s^(1<<to)][to] = min(dp[s^(1<<to)][to], 
                            dp[s][now]+dist(pos[now],
                                            pos[to])/speed)
      
ans = float('inf')

for s in range((1<<n)-1, 1<<(n+m), 1<<n):
  speed = 1
  for j in range(m):
    if s >> (n+j) & 1:
      speed *= 2
  for now in range(n+m):
    if not (s >> now) & 1:
      continue
    ans = min(ans, dp[s][now]+dist((0,0),pos[now])/speed)
   
print(ans)