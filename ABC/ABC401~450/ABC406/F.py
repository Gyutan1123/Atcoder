import sys
# import collections, heapq, string, math, itertools, copy, bisect, functools
# from sortedcontainers import SortedSet, SortedList, SortedDict

from atcoder import fenwicktree

# pypyで再帰書く時のおまじない
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

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
connect = [[] for _ in range(n)]
E = []
for _ in range(n-1):
  a,b = MI()
  connect[a-1].append(b-1)
  connect[b-1].append(a-1)
  E.append((a-1,b-1))

In = [0]*n
Out = [0]*n
i = 0
visited = [False]*n

def dfs(v):
  global i
  visited[v] = True
  In[v] = i
  i += 1
  for to in connect[v]:
    if not visited[to]:
      dfs(to)
  Out[v] = i

dfs(0)

BIT = fenwicktree.FenwickTree(n)
for i in range(n):
  BIT.add(i, 1)

q = II()
for _ in range(q):
  query = LI()
  if query[0] == 1:
    BIT.add(In[query[1]-1], query[2])
  else:
    u,v = E[query[1]-1]
    
    if In[u] > In[v]:
      u,v = v,u
    w = BIT.sum(In[v],Out[v])
    all = BIT.sum(0,n)
    print(abs(all-2*w))