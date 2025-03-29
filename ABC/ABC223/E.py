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
mod = 10**9 + 7
########################################################
ans = 'No'
x,y,a,b,c = MI()

def check(x,y,a,b,c):
  global ans
  
  ay = (a+x-1)//x
  if (y-ay > 0 
      and ((b+(y-ay)-1)//(y-ay) + (c+(y-ay)-1)//(y-ay) <= x
      or (b+x-1)//x + (c+x-1)//x + ay <= y)):
    ans = 'Yes'
    
  ax = (a+y-1)//y
  if (x-ax > 0 
      and ((b+(x-ax)-1)//(x-ax) + (c+(x-ax)-1)//(x-ax) <= y)
      or (b+y-1)//y + (c+y-1)//y + ax <= x):
    ans = 'Yes'
    
check(x,y,a,b,c)
check(x,y,b,c,a)
check(x,y,c,a,b)

print(ans)