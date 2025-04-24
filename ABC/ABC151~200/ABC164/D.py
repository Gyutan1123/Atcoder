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

s = list(SI())
s = list(map(int,s))

R = [0]

for i in range(len(s)):
  R.append((R[-1]+s[i]*pow(10,len(s)-1-i,2019))%2019)

d = collections.Counter(R)

ans = 0
for k in d.keys():
  ans += d[k]*(d[k]-1)//2

print(ans)