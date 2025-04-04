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
mod = 998244353
########################################################
t = II()

for _ in range(t):
  n = II()
  s = SI()
  ans = 0
  for i in range(n//2):
    if n%2 == 0:
      ans += ((ord(s[i])-65)*pow(26,(n-2-2*i)//2,mod))%mod
    else:
      ans += (ord(s[i])-65)*pow(26,(n-2*i)//2,mod)%mod


  if n%2 == 0:
    tmp = ['']*n
    for i in range(n//2):
      tmp[i] = s[i]
      tmp[n-1-i] = s[i]
    if ''.join(tmp) <= s:
      ans += 1
  
  if n%2 == 1:
    ans += ord(s[n//2])-65
    tmp = ['']*n
    for i in range(n//2):
      tmp[i] = s[i]
      tmp[n-1-i] = s[i]
    tmp[n//2] = s[n//2]

    if ''.join(tmp) <= s:
      ans += 1

  print(ans%mod)