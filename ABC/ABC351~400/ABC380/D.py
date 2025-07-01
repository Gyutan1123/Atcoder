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

s = SI()
q = II()
K = LI()

def conversion(s, num):
  if num%2 == 0:
    return s
  else:
    if 'A' <= s <= 'Z':
      return s.lower()
    else:
      return s.upper()
  
ans = []

for k in K:
  if k <= len(s):
    ans.append(s[k-1])
  else:
    cnt = 0
    while True:
      cnt += 1
      tmp = k-len(s)
      
      l = 0
      r = 100
      
      while r-l > 1:
        mid = (l+r)//2
        if (pow(2,mid)-1)*len(s) >= tmp:
          r = mid
        else:
          l = mid
          
      offset = tmp-(pow(2,l)-1)*len(s)
      
      if offset <= len(s):
        ans.append(conversion(s[offset-1], cnt))
        break
      
      else:
        k = offset
        
print(*ans)