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

x = SI()
S = [0]
for i in range(len(x)):
  S.append(S[-1] + int(x[i]))

ans = []
carry = 0
for i in range(len(x)):
  num = S[-1-i]+carry
  s = num%10
  c = num//10
  ans.append(s)
  
  carry = c

if carry > 0:
  ans.append(carry)

ans.reverse()
print(*ans, sep="")  