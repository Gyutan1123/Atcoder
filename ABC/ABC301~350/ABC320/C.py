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

m = II()
S1 = SI()
S2 = SI()
S3 = SI()

S = [S1, S2, S3]


s = []
for i in range(10):
  if str(i) in S1 and str(i) in S2 and str(i) in S3:
    s.append(str(i))
  
if len(s) == 0:
  print(-1)
  exit()

ans = float('inf')
for i in s:
  for p in itertools.permutations(range(3)):
    now = -1
    vis = [False]*3
    while not all(vis):
      for k in range(m):
        now += 1
        if S[p[0]][k] == i and vis[0] == False:
          vis[0] = True
        elif S[p[1]][k] == i and vis[1] == False:
          vis[1] = True
        elif S[p[2]][k] == i and vis[2] == False:
          vis[2] = True
        if all(vis):
          break
    ans = min(ans, now)
print(ans)
