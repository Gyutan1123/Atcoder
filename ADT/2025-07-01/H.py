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

n,q = MI()

d = dict()
for i in range(n):
  d[i] = (i,i,i)
  
num = [1]*n
  
UF = UnionFind(n)
for _ in range(q):
  query = LI()
  if query[0] == 1:
    x,c = query[1]-1,query[2]-1
    
    l,r,color = d[UF.leader(x)]
    if color == c:
      continue
    
    num[color] -= UF.size(x)
    num[c] += UF.size(x)
    
    if l > 0 and d[UF.leader(l-1)][2] == c:
      new_l = d[UF.leader(l-1)][0]
      UF.merge(l-1,x)
      l = new_l
    
    if r < n-1 and d[UF.leader(r+1)][2] == c:
      new_r = d[UF.leader(r+1)][1]
      UF.merge(r+1,x)
      r = new_r
    
    d[UF.leader(x)] = (l,r,c)
  
  
  else:
    c = query[1]-1
    print(num[c])