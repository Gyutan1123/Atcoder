import sys
import collections, heapq, string, math, itertools, copy, bisect, functools
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

class UnionFind:
  def __init__(self,n):
    self.n=n
    self.parent_size=[-1]*n

  def leader(self,a):
    if self.parent_size[a]<0: return a
    self.parent_size[a]=self.leader(self.parent_size[a])
    return self.parent_size[a]

  def merge(self,a,b):
    x,y=self.leader(a),self.leader(b)
    if x == y: return 
    if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
    self.parent_size[x] += self.parent_size[y]
    self.parent_size[y]=x
    return 

  def same(self,a,b):
    return self.leader(a) == self.leader(b)

  def size(self,a):
    return abs(self.parent_size[self.leader(a)])

  def groups(self):
    result=[[] for _ in range(self.n)]
    for i in range(self.n):
      result[self.leader(i)].append(i)
    return [r for r in result if r != []]

n,m = MI()
A = LI()

UF = UnionFind(n+1)
for a in A:
  UF.merge(a,a+1)

ans = []

vis = [False]*(n+1)

for i in range(1,n+1):
  if not vis[i]:
    for g in UF.groups():
      if i in g:
        g.sort(reverse=True)
        for j in g:
          vis[j] = True
          ans.append(j)
  
print(*ans)