import sys
import collections, heapq, string, math, itertools, copy, bisect, functools
from sortedcontainers import SortedSet, SortedList, SortedDict
import networkx as nx

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

n = II()
g = nx.Graph()
D = [LI() for _ in range(n-1)]
for i in range(n-1):
  for j in range(i+1,n):
    g.add_edge(i,j,weight=D[i][j-i-1])
  
d = nx.max_weight_matching(g)

ans = 0
for e in d:
  ans += g[min(e)][max(e)]['weight']
print(ans)