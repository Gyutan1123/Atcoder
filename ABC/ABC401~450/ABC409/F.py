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
nowNodeNum = n
XY = [LI() for _ in range(n)]

heap = []
for i in range(n):
  for j in range(i+1,n):
    x1, y1 = XY[i]
    x2, y2 = XY[j]
    dist = abs(x1-x2)+abs(y1-y2)
    heapq.heappush(heap, (dist, i, j)) 

queries = []
for _ in range(q):
  query = LI()
  if query[0] == 1:
    n += 1
  queries.append(query)
 
UF = UnionFind(n)


for query in queries:
  if query[0] == 1:
    xnew,ynew = query[1:]
    XY.append([xnew,ynew])
    for i in range(nowNodeNum):
      x,y = XY[i]
      dist = abs(xnew-x)+abs(ynew-y)
      heapq.heappush(heap, (dist, i, nowNodeNum))
    nowNodeNum += 1
  
  if query[0] == 2:
    if len(UF.groups())-(n-nowNodeNum) == 1:
      print(-1)
      continue
    dist, i,j = heapq.heappop(heap)
    while UF.same(i,j) and heap:
      dist,i,j = heapq.heappop(heap)
    print(dist)
    UF.merge(i,j)
    while heap and dist == heap[0][0]:
      _,i,j = heapq.heappop(heap)
      if not UF.same(i,j):
        UF.merge(i,j)
  
  if query[0] == 3:
    u,v = query[1:]
    if UF.same(u-1, v-1):
      print("Yes")
    else:
      print("No")
