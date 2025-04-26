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

h,w = MI()

C = [SI() for _ in range(h)]

D = collections.defaultdict(lambda:'.')

for i in range(h):
  for j in range(w):
    D[(i,j)] = C[i][j]

n = min(h,w)
ans = []
for i in range(1,n+1):
  tmp = 0
  for a in range(h):
    for b in range(w):
      if D[(a,b)] != '#':
        continue
    
      flag = True
      for d in range(1,i+1):
        if (D[(a+d,b+d)] == '.' 
            or D[(a+d,b-d)] == '.'
            or D[(a-d,b+d)] == '.'
            or D[(a-d,b-d)] == '.'):
          flag = False
      
      if (D[(a+i+1,b+i+1)] == '#' 
          and D[(a+i+1,b-i-1)] == '#' 
          and D[(a-i-1,b+i+1)] == '#'
          and D[(a-i-1,b-i-1)] == '#'):
        flag = False
      
      if flag:
        tmp += 1
  ans.append(tmp)
  
print(*ans)