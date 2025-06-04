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

n = II()

def solv_quadratic_equation(a, b, c):
    """ 2次方程式を解く  """
    D = (b**2 - 4*a*c) ** (1/2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)
    
    return x_1, x_2
  
for k in range(1,10**6+10):
  if n%(k) != 0:
    continue
  else:
    a = 3
    b = 3*k
    c = k**2-n//k
    
    if b**2 - 4*a*c < 0:
      continue
    y1, y2 = solv_quadratic_equation(a, b, c)
    

    y1 = int(y1)
    y2 = int(y2)
    
    x1 = y1+k
    x2 = y2+k
    
    if x1**3-y1**3 == n and x1 > 0 and y1 > 0:
      print(x1, y1)
      exit()
    elif x2**3-y2**3 == n and x2 > 0 and y2 > 0:
      print(x2, y2)
      exit()
      
print(-1)
