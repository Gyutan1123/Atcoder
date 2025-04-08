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

n,q,x = MI()
w = LI()

s = [0]
for i in range(n):
  s.append(s[-1]+w[i])

f = [-1]*n

for i in range(n):
  tmp = x
  count = 0
  r = 0
  if s[n]-s[i] < tmp:
    tmp -= (s[n]-s[i])
    count += n-i

    count += tmp//s[n]*n
    tmp -= tmp//s[n]*s[n]
    if tmp > 0:
      l = 0
      r = n
      while r-l > 1:
        mid = (r+l)//2
        if s[mid] >= tmp:
          r = mid
        else:
          l = mid
      count += r
    f[i] = (r%n,count)
    continue

  l = 0
  r = n
  while r-l > 1:
    mid = (r+l)//2
    if s[mid] - s[i] >= tmp:
      r = mid
    else:
      l = mid

  f[i] = (r%n,r-i)

k = 50

dp = [[-1]*n for _ in range(k+1)]

for i in range(n):
  dp[0][i] = f[i][0]
  
for i in range(k):
  for j in range(n):
    dp[i+1][j] = dp[i][dp[i][j]]


for _ in range(q):
  k = II()
  k -= 1
  now = 0
  i = 0
  while k:
    if k & 1:
      now = dp[i][now]
    i += 1
    k = k >> 1

  print(f[now][1])