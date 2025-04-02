import sys
import collections, heapq, string, math, itertools, copy
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
# pypyjit.set_param('max_unroll_recursion=-1')
# import pypyjit

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
adj = [[False]*(n) for _ in range(n)]
adj2 = [[False]*(n) for _ in range(n)]
for i in range(m):
  a,b = MI()
  adj[a-1][b-1] = True
  adj[b-1][a-1] = True

for i in range(m):
  a,b = MI()
  adj2[a-1][b-1] = True
  adj2[b-1][a-1] = True

for p in itertools.permutations(range(n)):
  flag = True
  for i in range(n):
    for j in range(n):
      if adj[i][j] != adj2[p[i]][p[j]]:
        flag = False
  
  if flag:
    print('Yes')
    exit()
print('No')