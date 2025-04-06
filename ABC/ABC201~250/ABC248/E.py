import sys
import collections, heapq, string, math, itertools, copy
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


n,k = MI()
P = [LI() for _ in range(n)]

if k == 1:
  print('Infinity')
  exit()
  
ans = 0

s = set()

for p1,p2 in itertools.combinations(P,2):
  x1,y1 = p1
  x2,y2 = p2
  
  a = -(y2-y1)
  b = x2-x1
  c = x1*(y2-y1)-y1*(x2-x1)
  gcd = math.gcd(abs(a),abs(b),abs(c))
  
  a //= gcd
  b //= gcd
  c //= gcd
  
  if a < 0:
    a *= -1
    b *= -1
    c *= -1
  if a == 0 and b < 0:
    b *= -1
    c *= -1
  
  if (a,b,c) in s:
    continue
  
  s.add((a,b,c))

  def l(x,y):
    return a*x+b*y+c
    
  count = 0
  for p in P:
    x,y = p
    if l(x,y) == 0:
      count += 1
      
  if count >= k:
    ans += 1
    
print(ans)