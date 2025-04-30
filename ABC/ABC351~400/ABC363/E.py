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
  
h,w,y = MI()
A = [LI() for _ in range(h)]

UF = UnionFind(h*w+1)

D = [(-1,0), (1,0), (0,-1), (0,1)]
dic = collections.defaultdict(list)

for i in range(h):
  for j in range(w):
    dic[A[i][j]].append((i,j))
    
    
for i in range(1,y+1):
  for x,y in dic[i]:
    for dx,dy in D:
      if 0 <= x+dx < h and 0 <= y+dy < w:
        if A[x+dx][y+dy] <= A[x][y]:
          UF.merge(x*w+y, (x+dx)*w+(y+dy))
      else:
        UF.merge(x*w+y, h*w)
        
  print(h*w-UF.size(h*w)+1)