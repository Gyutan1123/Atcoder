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
mod = 998244353
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
UF = UnionFind(n+1)
cycle = set() 
cycleNum = 0
flag = True
for _ in range(m):
  u,v = MI()
  if not UF.same(u,v):
    # 2つの閉路を結んでしまう
    if UF.leader(u) in cycle and UF.leader(v) in cycle:
      flag = False
    # 閉路ありの連結成分を拡大
    if UF.leader(u) in cycle or UF.leader(v) in cycle:
      cycle.add(UF.leader(u))
      cycle.add(UF.leader(v))
    UF.merge(u,v)
    
  else:
    # 2つめの閉路を作ってしまう
    if UF.leader(u) in cycle:
      flag = False
    else:
      cycle.add(UF.leader(u))
      cycleNum +=1


for i in range(1,n+1):
  # サイクルがない
  if not UF.leader(i) in cycle:
    flag = False
    
if cycleNum > 0 and flag:
  print(pow(2,cycleNum,mod))
else:
  print(0)