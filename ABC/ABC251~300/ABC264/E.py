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

n,m,e = MI()

UV = [LI() for _ in range(e)]

q = II()
X = [II() for _ in range(q)]
X.reverse()
xs = set(X)

UF = UnionFind(n+2)

for i in range(e):
  if not i+1 in xs:
    u,v = UV[i]
    UF.merge(min(u,n+1),min(v,n+1))
    
ans = 0
for i in range(1,n+1):
  if UF.same(i,n+1):
    ans += 1
    
ansl = []
ansl.append(ans)

for x in X:
  u,v = UV[x-1]
  u = min(u,n+1)
  v = min(v,n+1)
  
  if not UF.same(u,n+1) and not UF.same(v,n+1):
    UF.merge(u,v)
  elif UF.same(u,n+1) and not UF.same(v,n+1):
    ans += UF.size(v)
    UF.merge(u,v)
  elif not UF.same(u,n+1) and UF.same(v,n+1):
    ans += UF.size(u)
    UF.merge(u,v)
  
  ansl.append(ans)
  
for a in reversed(ansl[:-1]):
  print(a)