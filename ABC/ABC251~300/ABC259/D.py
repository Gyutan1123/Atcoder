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

n = II()
UF = UnionFind(n)

sx,sy,tx,ty = MI()

C = [LI() for _ in range(n)]

for i in range(n):
  for j in range(i+1,n):
    xi,yi,ri = C[i]
    xj,yj,rj = C[j]
    if (ri-rj)**2 <= (xi-xj)**2 + (yi-yj)**2 <= (ri+rj)**2:
      UF.merge(i,j)
    
for i in range(n):
  xi,yi,ri = C[i]
  if (sx-xi)**2 + (sy-yi)**2 == ri**2:
    si = i
  
for i in range(n):
  xi,yi,ri = C[i]
  if (tx-xi)**2 + (ty-yi)**2 == ri**2:
    ti = i

print('Yes' if UF.same(si,ti) else 'No')