import sys
import collections, heapq, string
II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

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
    
h,w = MI()

UF = UnionFind((h+1)*(w+1))

q = II()

grid = [['w']*(w+1) for _ in range(h+1)]
dire = [(-1,0),(1,0),(0,-1),(0,1)]

for _ in range(q):
  query = LI()
  
  if query[0] == 1:
    grid[query[1]][query[2]] = 'r'
    for d in dire:
        next = (query[1]+d[0],query[2]+d[1])
        if (1 <= next[0] <= h 
            and 1 <= next[1] <= w
            and grid[next[0]][next[1]] == 'r'
            ):
          UF.merge((next[0]-1)*w + next[1], 
                   (query[1]-1)*w + query[2])      
  elif (grid[query[1]][query[2]] == 'r' 
          and grid[query[3]][query[4]] == 'r'
          and UF.same((query[1]-1)*w + query[2],
                      (query[3]-1)*w + query[4])
          ):
    print('Yes')
  else:
    print('No')
        
            

  
  
  