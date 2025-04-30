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

tmp = n-1
for d in range(1,50):
  if d == 1:
    num = 10
  else:
    num = 9*pow(10, (d+1)//2-1)

  if tmp-num >= 0:
    tmp -= num
  else:
    if d == 1:
      print(n-1)
      exit()
    
    ans = []
    if d%2 == 0:
      a = tmp//(pow(10,(d-2)//2))
      tmp -= a*pow(10,(d-2)//2)
      ans.append(str(a+1))
      
      for i in range(2,d//2+1):
        a = tmp//(pow(10,(d-2*i)//2))
        tmp -= a*pow(10,(d-2*i)//2)
        ans.append(str(a))
      
      ans += ans[::-1]
    
    if d%2 == 1:
      a = tmp//pow(10,(d-2)//2 + 1)
      tmp -= a*pow(10,(d-2)//2 + 1)
      ans.append(str(a+1))
      
      for i in range(2, d//2+1):
        a = tmp//(pow(10,(d-2*i)//2+1))
        tmp -= a*pow(10,(d-2*i)//2+1)
        ans.append(str(a))
      
      ans = ans+[str(tmp)]+ans[::-1]
      
    print(''.join(ans))    
    exit()
    
    