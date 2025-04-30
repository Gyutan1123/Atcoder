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

n = II()

L = [0,10]

for l in range(2,50):
  if l%2 == 0:
    L.append(L[-1]+9*pow(10,(l-1)//2))
  else:
    L.append(L[-1]+9*pow(10,l//2))

l = bisect.bisect_left(L,n)

if l == 1:
  print(n-1)
  exit()

tmp = n-L[l-1]-1

ans = []
if l%2 == 0:
  a1 = tmp//(pow(10,(l-2)//2))
  ans.append(a1+1)
  tmp -= a1*pow(10,(l-2)//2)
  for j in range(2,l//2+1):
    a = tmp//(pow(10,(l-2*j)//2))
    ans.append(a)
    tmp -= a*pow(10,(l-2*j)//2)

  print(''.join(map(str, ans+ans[::-1])))
else:
  a1 = tmp//(pow(10,(l-2)//2+1))
  ans.append(a1+1)
  tmp -= a1*pow(10,(l-2)//2+1)
  for j in range(2,l//2+1):
    a = tmp//(pow(10,(l-2*j)//2+1))
    ans.append(a)
    tmp -= a*pow(10,(l-2*j)//2+1)

  a = tmp%10
  ans.append(a)
  ans += reversed(ans[:-1])

  print(''.join(map(str, ans)))