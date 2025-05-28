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

n,m = MI()
X = LI()
ans = [0]*(n+1)
now = X[0]-1
nobreak = 0
for i in range(m-1):
  nxt = X[i+1]-1
  nobreak += min(abs(nxt-now), abs((abs(nxt-now)-n)))
  if nxt > now:
    # 順方向に回る
    if nxt-now < abs(nxt-now-n):
      diff = abs(nxt-now-n)-(nxt-now)
      ans[now] += diff
      ans[nxt] -= diff
    # 逆方向に回る
    elif nxt-now > abs(nxt-now-n):
      diff = nxt-now-abs(nxt-now-n)
      ans[nxt] += diff
      ans[n] -= diff
      ans[0] += diff
      ans[now] -= diff
  else:
    # 逆方向に回る
    if abs(nxt-now) < abs((abs(nxt-now)-n)):
      diff = abs((abs(nxt-now)-n))-(abs(nxt-now))
      ans[nxt] += diff
      ans[now] -= diff
    # 順方向に回る
    elif abs(nxt-now) > abs((abs(nxt-now)-n)):
      diff = abs(nxt-now)-abs((abs(nxt-now)-n))
      ans[now] += diff
      ans[n] -= diff
      ans[0] += diff
      ans[nxt] -= diff
      
  now = nxt

for i in range(n):
  ans[i+1] += ans[i]

print(min(ans[:n])+nobreak)