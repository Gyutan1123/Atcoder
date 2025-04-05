import sys
import collections, heapq, string, math, itertools

II = lambda: int(sys.stdin.readline().rstrip())
SI = lambda: sys.stdin.readline().rstrip()
MI = lambda: map(int, sys.stdin.readline().rstrip().split())
MS = lambda: sys.stdin.readline().rstrip().split()
LI = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
LS = lambda: list(sys.stdin.readline().rstrip().split())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

n,r,c = MI()
S = list(SI())

kemuri = set()
kemuri.add((0,0))

o1 = 0
o2 = 0

ans = []

for s in S:
  
  if s == 'N':
    r += 1
    o1 += 1
  if s == 'W':
    c += 1
    o2 += 1
  if s == 'S':
    r -= 1
    o1 -=1
  if s == 'E':
    c -= 1
    o2 -= 1
    
  if (r,c) in kemuri:
    
    ans.append('1')
  else:
    ans.append('0')
  
  if not (o1,o2) in kemuri:
    kemuri.add((o1,o2))
  

print(''.join(ans))