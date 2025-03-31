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
mod = 998244353
########################################################

h,w,k = MI()
x1,y1,x2,y2 = MI()

dp00 = [0]*(k+1)
dp01 = [0]*(k+1)
dp10 = [0]*(k+1)
dp11 = [0]*(k+1)

if x1 == x2 and y1 == y2:
  dp11[0] = 1
elif x1 == x2:
  dp10[0] = 1
elif y1 == y2:
  dp01[0] = 1
else:
  dp00[0] = 1

for i in range(k):
  dp00[i+1] = ((h+w-4)*dp00[i]+(w-1)*dp01[i]+(h-1)*dp10[i])%mod
  dp01[i+1] = (dp00[i]+(h-2)*dp01[i]+(h-1)*dp11[i])%mod
  dp10[i+1] = (dp00[i]+(w-2)*dp10[i]+(w-1)*dp11[i])%mod
  dp11[i+1] = (dp01[i]+dp10[i])%mod

print(dp11[k]%mod)
